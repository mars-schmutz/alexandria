const { contextBridge, ipcRenderer } = require('electron')

contextBridge.exposeInMainWorld("alexandria", {
    addAsset: () => ipcRenderer.send("add-asset"),

    getSettingsPage: (callback) => ipcRenderer.on("nav-settings", callback),
})

contextBridge.exposeInMainWorld("store", {
    get: (key) => ipcRenderer.invoke("store:get", key),
})