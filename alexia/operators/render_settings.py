import bpy
import json
import inspect
import mathutils

from bpy_extras.io_utils import ExportHelper, ImportHelper

blacklist = ["__doc__", "__module__", "__slots__", "bl_rna", "rna_type", "__annotations__", "__dict__", "__doc__", "__module__", "__weakref__", "_devices_update_callback", "register", "unregister", "gi_cache_info"]

def load_eevee(settings_dict):
    prefix = bpy.data.scenes["Scene"].eevee
    for key, value in settings_dict.items():
        if type(value) == list:
            if value[0] == "c":
                color = mathutils.Color((value[1], value[2], value[3]))
                setattr(prefix, key, color)
        else:
            setattr(prefix, key, value)

def load_cycles(settings_dict):
    prefix = bpy.data.scenes["Scene"].cycles
    for key, value in settings_dict.items():
        if type(value) == list:
            if value[0] == "c":
                color = mathutils.Color((value[1], value[2], value[3]))
                setattr(prefix, key, color)
        else:
            setattr(prefix, key, value)

class ALEXIA_OT_ExportRenderSettings(bpy.types.Operator, ExportHelper):
    bl_idname = "alexia.export_render_settings"
    bl_label = "Render Settings"
    bl_description = "Export render settings to a JSON file"

    filename_ext = ".json"

    def execute(self, ctx):
        engine = bpy.data.scenes["Scene"].render.engine
        prefix = None
        if engine == "CYCLES":
            prefix = bpy.data.scenes["Scene"].cycles
        elif engine == "BLENDER_EEVEE":
            prefix = bpy.data.scenes["Scene"].eevee
        else:
            self.report({"ERROR"}, "Unsupported render engine")
            return {"CANCELLED"}

        render_settings = {
            "engine": engine,
        }
        attrs = inspect.getmembers(prefix)

        for attr in attrs:
            if attr[0] not in blacklist:
                if type(attr[1]) == mathutils.Color:
                    # index 0 is the attribute type
                    render_settings[attr[0]] = ["c", attr[1].r, attr[1].g, attr[1].b]
                else:
                    render_settings[attr[0]] = attr[1]
        
        # export to json
        if self.filepath != "":
            fobj = open(self.filepath, "w")
            json.dump(render_settings, fobj)
            fobj.close()
            return {"FINISHED"}
        else:
            return {"CANCELLED"}

class ALEXIA_OT_ImportRenderSettings(bpy.types.Operator, ImportHelper):
    bl_idname = "alexia.import_render_settings"
    bl_label = "Render Settings"
    bl_description = "Import render settings from a JSON file"
    bl_options = {"REGISTER", "UNDO"}

    filename_ext = ".json"

    def execute(self, ctx):
        alexia = ctx.scene.alexia
        library = ctx.scene.library
        asset = library[alexia.asset_index]
        self.filepath = asset.assetPath
        render_settings = {}

        if self.filepath != "":
            fobj = open(self.filepath, "r")
            render_settings = json.load(fobj)
            fobj.close()
            engine = render_settings["engine"]
            del render_settings["engine"]
            if engine == "BLENDER_EEVEE":
                load_eevee(render_settings)
            elif engine == "CYCLES":
                load_cycles(render_settings)
            else:
                self.report({"ERROR"}, "Unsuported render engine")
                return {"CANCELLED"}
            return {"FINISHED"}
        else:
            self.report({"ERROR"}, "No file selected")
            return {"CANCELLED"}