const { app, BrowserWindow, Menu, ipcMain, dialog } = require("electron")
const Store = require("electron-store")
const path = require("path")
// const menu = require("./menu")
const schema = require("./schema")
const menuTemplate = require("./menu2")

const store = new Store(schema)
let libraryLocation;
let mainWin;

async function handleFileDialog() {
  const { canceled, filePaths } = await dialog.showOpenDialog({
    properties: ["openDirectory", "createDirectory"],
  });
  if (canceled) {
    return
  } else {
    return filePaths[0]
  }
}

function createWindow(w, h, parent, url) {
  const win = new BrowserWindow({
    width: w,
    height: h,
    parent: parent,
    webPreferences: {
      preload: path.join(__dirname, "preload.js")
    }
  })

  win.loadFile(url)
  return win;
}

app.whenReady().then(() => {
  mainWin = createWindow(800, 600, null, "dist/index.html")
  const template = menuTemplate("Alexandria", mainWin, createWindow)
  const menu = Menu.buildFromTemplate(template)
  Menu.setApplicationMenu(menu)
  libraryLocation = store.get("library-location")

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      mainWin = createWindow(900, 700, null, "dist/index.html")
    }
  })

  ipcMain.handle("store:get", (event, key) => {
    return store.get(key)
  })

  ipcMain.handle("store:set", (event, key, value) => {
    return store.set(key, value)
  })

  ipcMain.handle("dialog:open-file", handleFileDialog)
  // ipcMain.handle("get-prefs", getPrefsPath)
  ipcMain.handle("get-prefs", () => {
    return app.getPath("userData")
  })
})

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit()
  }
})