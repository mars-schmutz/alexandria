const isMac = process.platform === 'darwin'
const createMenuTemplate = (name, mainWin, createWindow) => {
    return [
        ...(isMac ? [{
            label: name,
            submenu: [
                { role: 'about' },
                {
                    label: 'Settings',
                    click: () => { mainWin.webContents.send("nav-settings") },
                    accelerator: "Cmd+,"
                },
                { type: 'separator' },
                { role: 'services' },
                { type: 'separator' },
                { role: 'hide' },
                { role: 'hideothers' },
                { role: 'unhide' },
                { type: 'separator' },
                { role: 'quit' }
            ]
        }] : []),
        {
            label: 'File',
            submenu: [
                {
                    label: 'Open Library',
                    click: () => { createWindow(400, 300, mainWin, "dist/index.html") }
                },
                {
                    label: "Settings",
                    click: () => { mainWin.webContents.send("nav-settings") },
                },
                isMac ? { role: 'close' } : { role: 'quit' }
            ]
        },
        {
            label: "View",
            submenu: [
                { role: "reload" },
                { role: "forcereload" },
                { role: "toggledevtools" },
            ]
        }
    ]
}

module.exports = createMenuTemplate