import bpy
import json
import mathutils
from bpy_extras.io_utils import ImportHelper, ExportHelper

blacklist = ["rna_type", "hops", "inputs", "internal_links", "outputs", "scene"]
def exportCompositor(filepath):
    nodes = bpy.context.scene.node_tree.nodes
    nodeInfo = {}
    conns = []

    for node in nodes:
        inputs = {}
        attrs = {}
        for prop in dir(node):
            attr = getattr(node, prop)
            if not prop.startswith("__") and not prop.startswith("bl_") and not callable(attr) and prop not in blacklist:
                print(f"WOrking on prop {prop}, {getattr(node, prop)}")
                if bpy.types.bpy_struct.is_property_readonly(node, prop):
                    print(f"{prop} is readonly")
                    continue
                # looks like blender converts to the type so i don't need labels
                if isinstance(attr, mathutils.Color):
                    tmp = [attr.r, attr.g, attr.b]
                    attr = tmp
                elif isinstance(attr, mathutils.Vector):
                    tmp = [attr.to_tuple()]
                    attr = tmp
                attrs[prop] = attr
        for sock in node.inputs:
            if sock.is_linked:
                for link in sock.links:
                    conns.append([link.from_node.name, link.from_socket.identifier, node.name, sock.identifier])
            else:
                if sock.type == "VALUE":
                    inputs[sock.name] = sock.default_value
                elif sock.type == "RGBA":
                    inputs[sock.name] = [val for val in sock.default_value]
                elif sock.type == "VECTOR":
                    inputs[sock.name] = [val for val in sock.default_value]
        print()

        nodeInfo[node.name] = {
            "type": node.bl_idname,
            "inputs": inputs,
            "attrs": attrs
        }
    
    connList = []
    for conn in conns:
        newConn = {
            "fromNode": conn[0],
            "fromSock": conn[1],
            "toNode": conn[2],
            "toSock": conn[3]
        }
        connList.append(newConn)
    
    fullAsset = {
        "nodes": nodeInfo,
        "conns": connList
    }

    fobj = open(filepath, "w")
    json.dump(fullAsset, fobj)
    fobj.close()

def importCompositor(filepath):
    fobj = open(filepath, "r")
    data = json.load(fobj)
    fobj.close()

    bpy.context.scene.use_nodes = True
    nodes = bpy.context.scene.node_tree.nodes
    for node in nodes:
        nodes.remove(node)

    for node in data["nodes"]:
        nodeData = data["nodes"][node]
        newNode = nodes.new(nodeData["type"])
        for attr in nodeData["attrs"]:
            setattr(newNode, attr, nodeData["attrs"][attr])
        for input in nodeData["inputs"]:
            setattr(newNode.inputs[input], "default_value", nodeData["inputs"][input])
    
    for conn in data["conns"]:
        fromNode = nodes[conn["fromNode"]]
        fromSock = fromNode.outputs[conn["fromSock"]]
        toNode = nodes[conn["toNode"]]
        toSock = toNode.inputs[conn["toSock"]]
        bpy.context.scene.node_tree.links.new(fromSock, toSock)

class ALEXIA_OT_ExportCompositor(bpy.types.Operator, ExportHelper):
    bl_idname = "alexia.export_compositor"
    bl_label = "Export Compositor"
    bl_description = "Export the compositor to a JSON file"

    filename_ext = ".json"

    def execute(self, ctx):
        exportCompositor(self.filepath)
        return {"FINISHED"}

class ALEXIA_OT_ImportCompositor(bpy.types.Operator, ImportHelper):
    bl_idname = "alexia.import_compositor"
    bl_label = "Import Compositor"
    bl_description = "Import the compositor from a JSON file"

    filename_ext = ".json"

    def execute(self, ctx):
        alexia = ctx.scene.alexia
        library = ctx.scene.library
        asset = library[alexia.asset_index]
        self.filepath = asset.assetPath
        importCompositor(self.filepath)
        return {"FINISHED"}