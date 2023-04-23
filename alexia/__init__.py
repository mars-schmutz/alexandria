# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Alexia",
    "author": "Mersh",
    "version": (0, 0, 1),
    "blender": (3, 4, 0),
    "location": "3D View",
    "description": "Load assets created from Alexandria",
    "warning": "This project is still under development.",
    "category": "3D View"
}

import bpy
import json
from bpy.types import PropertyGroup
from bpy.props import StringProperty, PointerProperty, CollectionProperty

from . import library_settings
from . ui.panels import ALEXIA_PT_AssetView, ALEXIA_UL_assetlist
from . operators.load_asset import ALEXIA_OT_LoadAsset
from . operators.render_settings import ALEXIA_OT_ExportRenderSettings, ALEXIA_OT_ImportRenderSettings
from . operators.proc_material import ALEXIA_OT_ExportMaterial, ALEXIA_OT_ImportMaterial
from . operators.lights import ALEXIA_OT_ExportLights, ALEXIA_OT_ImportLights
from . operators.compositor import ALEXIA_OT_ExportCompositor, ALEXIA_OT_ImportCompositor

from . import handlers

# TODO: consider using asset path to directly retrieve the asset instead of using id to lookup in the library
class Entry(PropertyGroup):
    name: bpy.props.StringProperty(name = "Asset Name")
    assetId: bpy.props.StringProperty(name = "Asset ID")
    assetType: bpy.props.StringProperty(name = "Asset Type")
    assetPath: bpy.props.StringProperty(name = "Asset Path")

class ALEXIAProperties(PropertyGroup):

    render_settings_name: StringProperty(
        name = "New Render Asset",
        description = "Name of the new render settings asset",
        default = ""
    )

    assets: CollectionProperty(
        type = Entry,
        name = "Assets"
    )

    asset_index: bpy.props.IntProperty(
        name = "Asset Index",
        description = "Index of the active asset",
        default = 0
    )

def export_render(self, ctx):
    self.layout.operator(ALEXIA_OT_ExportRenderSettings.bl_idname)

def export_lights(self, ctx):
    self.layout.operator(ALEXIA_OT_ExportLights.bl_idname)

def export_material(self, ctx):
    self.layout.operator(ALEXIA_OT_ExportMaterial.bl_idname)

def export_compositor(self, ctx):
    self.layout.operator(ALEXIA_OT_ExportCompositor.bl_idname)

classes = (
    Entry,
    ALEXIAProperties,
    # Preferences
    library_settings.ALEXIAPreferences,
    library_settings.ALEXIA_OT_LoadLibrary,
    # Operators
    ALEXIA_OT_LoadAsset,
    ALEXIA_OT_ExportRenderSettings,
    ALEXIA_OT_ImportRenderSettings,
    ALEXIA_OT_ExportMaterial,
    ALEXIA_OT_ImportMaterial,
    ALEXIA_OT_ExportLights,
    ALEXIA_OT_ImportLights,
    ALEXIA_OT_ExportCompositor,
    ALEXIA_OT_ImportCompositor,
    # Panels
    ALEXIA_UL_assetlist,
    ALEXIA_PT_AssetView,
)

def register():
    from bpy.utils import register_class
    for c in classes:
        register_class(c)
    bpy.types.TOPBAR_MT_file_export.append(export_render)
    bpy.types.TOPBAR_MT_file_export.append(export_lights)
    bpy.types.TOPBAR_MT_file_export.append(export_material)
    bpy.types.TOPBAR_MT_file_export.append(export_compositor)

    bpy.app.handlers.load_post.append(handlers.handler_load)
    bpy.types.Scene.alexia = PointerProperty(type = ALEXIAProperties)
    bpy.types.Scene.library = bpy.props.CollectionProperty(type = Entry)

def unregister():
    from bpy.utils import unregister_class
    for c in reversed(classes):
        unregister_class(c)
    bpy.types.TOPBAR_MT_file_export.remove(export_render)
    bpy.types.TOPBAR_MT_file_export.remove(export_lights)
    bpy.types.TOPBAR_MT_file_export.remove(export_material)
    bpy.types.TOPBAR_MT_file_export.remove(export_compositor)

    bpy.app.handlers.load_post.remove(handlers.handler_load)
    del bpy.types.Scene.alexia
    del bpy.types.Scene.library