import bpy
from .. library_settings import load_entries

# Input sockets for Principled BSDF Shader
BSDF_IN = {
    "diffuse": "Base Color",
    "specular": "Specular",
    "roughness": "Roughness",
    "metallic": "Metallic",
}

class ALEXIA_OT_LoadAsset(bpy.types.Operator):
    bl_idname = "alexia.load_asset"
    bl_label = "Load Asset"
    bl_description = "Load the selected asset into the scene."
    bl_options = { "REGISTER", "UNDO" }

    def execute(self, ctx):
        scene = ctx.scene
        alexia = scene.alexia
        library = scene.library
        asset = library[alexia.asset_index]

        if asset.assetType == "material":
            load_material(ctx, asset.assetId)
        elif asset.assetType == "render":
            bpy.ops.alexia.import_render_settings("EXEC_DEFAULT")
        elif asset.assetType == "lights":
            bpy.ops.alexia.import_lights("EXEC_DEFAULT")
        elif asset.assetType == "proc_mat":
            bpy.ops.alexia.import_proc_mat("EXEC_DEFAULT")
        elif asset.assetType == "compositor":
            bpy.ops.alexia.import_compositor("EXEC_DEFAULT")
        else:
            print("Asset type not supported: " + asset.assetType)

        return {"FINISHED"}

def load_material(ctx, id):
    entries = load_entries(ctx)
    asset = next((e for e in entries if e["id"] == id), None)
    for k in list(asset["maps"].keys()):
        if not asset["maps"][k]:
            del asset["maps"][k]

def create_material(asset):
    material = bpy.data.materials.new(asset["name"])
    material.use_nodes = True
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    principled = nodes.get("Principled BSDF")

    for k, v in asset["maps"].items():
        texture = nodes.new("ShaderNodeTexImage")
        texture.image = bpy.data.images.load(v)
        socket = BSDF_IN.get(k, k)
        if socket in ["Displacement", "Normal"]:
            pass
        else:
            links.new(texture.outputs[0], principled.inputs[socket])

    return material