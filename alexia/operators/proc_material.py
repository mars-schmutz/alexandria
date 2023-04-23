import bpy
import json
from bpy_extras.io_utils import ImportHelper, ExportHelper

def exportMat(material, filepath):
    nodes = material.node_tree.nodes
    name = bpy.context.active_object.active_material.name
    nodeInfo = {}
    conns = []

    for n in nodes:
        inputs = {}
        for sock in n.inputs:
            if sock.is_linked:
                for link in sock.links:
                    print(link)
                    conns.append([link.from_node.name, link.from_socket.identifier, n.name, sock.identifier])
            else:
                if sock.type == "VALUE":
                    inputs[sock.name] = sock.default_value
                elif sock.type == "RGBA":
                    inputs[sock.name] = [val for val in sock.default_value]
                elif sock.type == "VECTOR":
                    inputs[sock.name] = [val for val in sock.default_value]

        nodeInfo[n.name] = {
            "type": n.bl_idname,
            "inputs": inputs
        }

    connList = []
    for c in conns:
        newConn = {
            "fromNode": c[0],
            "fromSock": c[1],
            "toNode": c[2],
            "toSock": c[3]
        }
        connList.append(newConn)

    fullAsset = {
        "name": name,
        "nodes": nodeInfo,
        "conns": connList
    }

    fobj = open(filepath, "w")
    json.dump(fullAsset, fobj)
    fobj.close()

def importMat(filepath):
    fobj = open(filepath, "r")
    data = json.load(fobj)
    fobj.close()

    material = bpy.data.materials.new(name=data['name'])
    material.use_nodes = True
    tree = material.node_tree
    nodes = tree.nodes

    for node in nodes:
        nodes.remove(node)
    
    node_map = {}
    for node_name, node_data in data['nodes'].items():
        node = nodes.new(node_data['type'])
        node_map[node_name] = node
        
        for input_name, input_value in node_data['inputs'].items():
            input_socket = node.inputs.get(input_name)
            if input_socket is None:
                continue
            if isinstance(input_value, list):
                input_socket.default_value = tuple(input_value)
            else:
                input_socket.default_value = input_value
    
    for connection_data in data['conns']:
        from_node = node_map[connection_data['fromNode']]
        from_socket = from_node.outputs.get(connection_data['fromSock'])
        to_node = node_map[connection_data['toNode']]
        to_socket = to_node.inputs.get(connection_data['toSock'])
        if from_socket and to_socket:
            tree.links.new(from_socket, to_socket)
    
    return material

class ALEXIA_OT_ExportMaterial(bpy.types.Operator, ExportHelper):
    bl_idname = "alexia.export_proc_mat"
    bl_label = "Export Material"
    bl_description = "Export material to a JSON file"

    filename_ext = ".json"

    def execute(self, ctx):
        material = bpy.context.object.active_material
        if material is None:
            self.report({"ERROR"}, "No material selected")
            return {"CANCELLED"}
        else:
            exportMat(material, self.filepath)
            return {"FINISHED"}

class ALEXIA_OT_ImportMaterial(bpy.types.Operator, ImportHelper):
    bl_idname = "alexia.import_proc_mat"
    bl_label = "Import Material"
    bl_description = "Import material from a JSON file"

    filename_ext = ".json"

    def execute(self, ctx):
        alexia = ctx.scene.alexia
        library = ctx.scene.library
        asset = library[alexia.asset_index]
        self.filepath = asset.assetPath
        material = importMat(self.filepath)
        bpy.context.object.active_material = material
        return {"FINISHED"}