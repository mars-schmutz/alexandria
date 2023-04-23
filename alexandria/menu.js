const { app, Menu } = require('electron')
const createWindow = require('./main').createWindow

const isMac = process.platform === 'darwin'

function buildMenu() {
    const menu = [
        // { role: 'appMenu' }
        ...(isMac ? [{
            label: app.name,
            submenu: [
                { role: 'about' },
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
        // { role: 'fileMenu' }
        {
            label: 'File',
            submenu: [
                {
                    label: 'Open Library',
                    click: () => { createWindow(400, 300, null, "dist/index.html") }
                },
                isMac ? { role: 'close' } : { role: 'quit' }
            ]
        }
    ]

    Menu.setApplicationMenu(Menu.buildFromTemplate(menu))
}

module.exports = buildMenu