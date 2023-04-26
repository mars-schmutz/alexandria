# Alexandria & Alexia

Alexandria is a 3D asset management program I built for my senior project. Alexia is a small sister program designed as a Blender plugin.

![Alexandria Home](https://i.imgur.com/z4NzKZd.png)

## Alexandria
On open, navigate to Settings and specify a location for your library. This must be done before creating any assets and is only required once.
Once set, click on the New button to choose an asset type and add details. Alexandria is non-destructive, so anything you add (such as settings files or texture maps) will be copied to the library location.

![Settings](https://i.imgur.com/8sxGrFZ.png)

![Add Material](https://i.imgur.com/5dMgPae.png)

Alexandria currently supports the following asset types:
- Materials with texture maps
- Procedural materials (with Blender's shader nodes)
- Blender Render settings
- Blender Compositor nodes
- Light Rigs

## Alexia
Alexia is the helper plugin to help bring your assets into your scene. Once it's been installed, copy the path to Alexandria's catalog file. You can find this in the Alexandria Settings page. Once it's in, click Load to retrieve all the assets. Alexia doesn't have the ability to edit any of these asset entries, so all changes must be made in Alexandria.

![Plugin Settings](https://i.imgur.com/q6WzA8Q.png)

Select an asset and click Load Asset. This will load the asset into your scene, whether it's a material, render settings, or a light rig. Assets based on information from Blender can be exported as a JSON file in File > Export > [Asset type]. After export you can add the JSON file to Alexandria to create a new asset based on those settings.

![Plugin Panel](https://i.imgur.com/SRUF0ZS.png)

## Building & Installation Instructions
### For Alexandria
Use `npm install` to install the packages. Electron may need to be installed globally, see instructions [here](https://www.electronjs.org/docs/latest/tutorial/quick-start) for more. Use `npm run build:all` to build and launch the program. Use `npm run package` to build the executable located in the /alexandria/out directory.

## For Alexia
Make sure the directory /alexia is zipped. Install in Blender through Edit > Preferences > Add-Ons > Install. Navigate and select the zipped directory.
