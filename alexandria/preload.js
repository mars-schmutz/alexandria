const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld("alexandria", {
    // addAsset: () => ipcRenderer.send("add-asset"), dont need?
    createEntry: (pth) => ipcRenderer.invoke("create-entry", pth),
    copyFile: (src, dest) => ipcRenderer.invoke("copy-file", src, dest),
    openFile: (dir) => ipcRenderer.invoke("dialog:open-file", dir),
    deleteEntry: (pth) => ipcRenderer.invoke("delete-entry", pth),
    openEntry: (path) => ipcRenderer.invoke("open-entry", path),

    getSettingsPage: (callback) => ipcRenderer.on("nav-settings", callback),
    getPrefPath: (value) => ipcRenderer.invoke("get-prefs", value),
})

contextBridge.exposeInMainWorld("store", {
    get: (key) => ipcRenderer.invoke("store:get", key),
    set: (key, value) => ipcRenderer.invoke("store:set", key, value),
})