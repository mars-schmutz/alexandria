import bpy
from bpy.props import *
from bpy.types import (Panel, Menu, Operator, PropertyGroup, UIList)
import bpy.types

class ALEXIA_PT_AssetView(Panel):
    bl_idname = "ALEXIA_PT_assetview"
    bl_label = "Assets"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Alexia"

    def draw(self, ctx):
        layout = self.layout
        scene = ctx.scene
        alexia = scene.alexia
        row = layout.row()
        row.operator("alexia.load_library")
        row = layout.row()
        row.template_list("ALEXIA_UL_assetlist", "asset_list", scene, "library", alexia, "asset_index", rows = 5)
        row = layout.row()
        row.operator("alexia.load_asset")

class ALEXIA_UL_assetlist(UIList):
    def draw_item(self, ctx, layout, data, item, icon, active_data, active_propname, index):
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            ic = ""
            if item.assetType == "material" or item.assetType == "proc_mat":
                ic = "MATERIAL"
            elif item.assetType == "render":
                ic = "RESTRICT_RENDER_OFF"
            elif item.assetType == "compositor":
                ic = "NODE_COMPOSITING"
            elif item.assetType == "lights":
                ic = "LIGHT"
            else:
                print("Unknown asset type: " + item.assetType)
            layout.label(text = item.name, icon = ic)
        elif self.layout_type in {'GRID'}:
            layout.alignment = 'CENTER'
            layout.label(text = item.name, icon = 'OBJECT_DATAMODE')