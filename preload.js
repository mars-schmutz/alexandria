const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld("alexandria", {
    // addAsset: () => ipcRenderer.send("add-asset"), dont need?
    createEntry: (pth) => ipcRenderer.invoke("create-entry", pth),
    copyFile: (src, dest) => ipcRenderer.invoke("copy-file", src, dest),
    openFile: (dir) => ipcRenderer.invoke("dialog:open-file", dir),

    getSettingsPage: (callback) => ipcRenderer.on("nav-settings", callback),
    getPrefPath: (value) => ipcRenderer.invoke("get-prefs", value),
})

contextBridge.exposeInMainWorld("store", {
    get: (key) => ipcRenderer.invoke("store:get", key),
    set: (key, value) => ipcRenderer.invoke("store:set", key, value),
})