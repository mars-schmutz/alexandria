import bpy
from bpy.app.handlers import persistent

@persistent
def handler_load(scene):
    bpy.ops.alexia.load_library()