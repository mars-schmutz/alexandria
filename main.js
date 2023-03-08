const { app, BrowserWindow, Menu, ipcMain } = require("electron")
const Store = require("electron-store")
const path = require("path")
// const menu = require("./menu")
// const store = require("./myStore")
const menuTemplate = require("./menu2")

const store = new Store()
let mainWin;

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
  store.set("test", "test")

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      mainWin = createWindow(800, 600, null, "dist/index.html")
    }
  })

  ipcMain.handle("store:get", (event, key) => {
    return store.get(key)
  })
})

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit()
  }
})