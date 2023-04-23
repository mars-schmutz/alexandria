import bpy
import json
from bpy_extras.io_utils import ExportHelper, ImportHelper

def exportLights(lghts):
    output = {}
    lights = []
    for i in lghts:
        light = {}
        print(i)
        light["name"] = i.name
        light["type"] = i.data.type
        light["loc"] = i.location.to_tuple()
        light["rot"] = [i.rotation_euler.x, i.rotation_euler.y, i.rotation_euler.z]
        light["color"] = [i.data.color.r, i.data.color.g, i.data.color.b]
        light["energy"] = i.data.energy
        light["shadow"] = i.data.use_shadow
        if i.data.type == "POINT":
            light["radius"] = i.data.shadow_soft_size
        elif i.data.type == "SUN":
            light["angle"] = i.data.angle
        elif i.data.type == "SPOT":
            light["radius"] = i.data.shadow_soft_size
            light["spot_size"] = i.data.spot_size
            light["spot_blend"] = i.data.spot_blend
        elif i.data.type == "AREA":
            light["size"] = i.data.size
            light["shape"] = i.data.shape
        lights.append(light)
    output["lights"] = lights
    return output

def importLights(lghts):
    for i in lghts:
        bpy.ops.object.light_add(type = i["type"], location = i["loc"], rotation = i["rot"])
        bpy.context.object.data.color = i["color"]
        bpy.context.object.data.energy = i["energy"]
        bpy.context.object.data.use_shadow = i["shadow"]
        if i["type"] == "POINT":
            bpy.context.object.data.shadow_soft_size = i["radius"]
        elif i["type"] == "SUN":
            bpy.context.object.data.angle = i["angle"]
        elif i["type"] == "SPOT":
            bpy.context.object.data.shadow_soft_size = i["radius"]
            bpy.context.object.data.spot_size = i["spot_size"]
            bpy.context.object.data.spot_blend = i["spot_blend"]
        elif i["type"] == "AREA":
            bpy.context.object.data.size = i["size"]
            bpy.context.object.data.shape = i["shape"]
        bpy.context.object.name = i["name"]

class ALEXIA_OT_ExportLights(bpy.types.Operator, ExportHelper):
    bl_idname = "alexia.export_lights"
    bl_label = "Export Lights"
    bl_description = "Export lights to a JSON file"
    bl_options = {"REGISTER", "UNDO"}

    filename_ext = ".json"

    def execute(self, ctx):
        lights = []
        for i in ctx.scene.objects:
            if i.type == "LIGHT":
                lights.append(i)
        out = exportLights(lights)
        if self.filepath != "":
            fobj = open(self.filepath, "w")
            json.dump(out, fobj)
            fobj.close()
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

class ALEXIA_OT_ImportLights(bpy.types.Operator, ImportHelper):
    bl_idname = "alexia.import_lights"
    bl_label = "Import Lights"
    bl_description = "Import lights from a JSON file"
    bl_options = {"REGISTER", "UNDO"}

    filename_ext = ".json"

    def execute(self, ctx):
        alexia = ctx.scene.alexia
        library = ctx.scene.library
        asset = library[alexia.asset_index]
        self.filepath = asset.assetPath

        if self.filepath != "":
            fobj = open(self.filepath, "r")
            data = json.load(fobj)
            fobj.close()
            importLights(data["lights"])
            return {"FINISHED"}
        else:
            return {"CANCELLED"}