const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld("alexandria", {
    // addAsset: () => ipcRenderer.send("add-asset"), dont need?
    createEntry: (path) => ipcRenderer.invoke("create-entry", path),
    copyFile: (src) => ipcRenderer.invoke("copy-file", src),
    openFile: (dir) => ipcRenderer.invoke("dialog:open-file", dir),

    getSettingsPage: (callback) => ipcRenderer.on("nav-settings", callback),
    getPrefPath: (value) => ipcRenderer.invoke("get-prefs", value),
})

contextBridge.exposeInMainWorld("store", {
    get: (key) => ipcRenderer.invoke("store:get", key),
    set: (key, value) => ipcRenderer.invoke("store:set", key, value),
})