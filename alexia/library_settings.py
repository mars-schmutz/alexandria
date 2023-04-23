import bpy
import json
from bpy.props import StringProperty

class ALEXIAPreferences(bpy.types.AddonPreferences):
    bl_idname = "alexia"

    catalog_path: StringProperty(
            name = "Catalog Path",
            description = "Path to the catalog file (found in Alexandria settings)",
            default = "",
            subtype = "FILE_PATH"
    )

    library_path: StringProperty(
            name = "Library Path",
            description = "Path to the library folder (same as saved in Alexandria settings)",
            default = "",
            subtype = "DIR_PATH"
    )
    
    def draw(self, ctx):
        layout = self.layout
        box = layout.box()
        box.label(text = "Alexia Settings")
        box.prop(self, "catalog_path")
        box.operator("alexia.load_library")

class ALEXIA_OT_LoadLibrary(bpy.types.Operator):
    bl_idname = "alexia.load_library"
    bl_label = "Load Library"
    bl_description = "Load the library from the catalog file"

    def execute(self, ctx):
        entries = load_entries(ctx)
        bpy.context.scene.library.clear()
        for entry in entries:
            item = bpy.context.scene.library.add()
            item.name = entry["name"]
            item.assetId = entry["id"]
            item.assetType = entry["type"]
            if entry["type"] != "material":
                item.assetPath = entry["settings"]
            else:
                item.assetPath = ""
        return {"FINISHED"}

def load_entries(ctx):
    prefs = ctx.preferences.addons["alexia"].preferences
    path = prefs.catalog_path
    entries = []
    try:
        fobj = open(path, "r")
        settings = json.load(fobj)
        fobj.close()
        entries = settings["library-shelves"]
    except:
        print("Could not load entries")
    return entries