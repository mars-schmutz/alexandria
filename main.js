const { app, BrowserWindow, Menu, ipcMain, dialog } = require("electron")
const fs = require("fs")
const Store = require("electron-store")
const path = require("path")
// const menu = require("./menu")
const schema = require("./schema")
const menuTemplate = require("./menu2")

const store = new Store(schema)
let libraryLocation;
let mainWin;

async function handleFileDialog(event, dir) {
  let props = []
  if (dir) {
    props = ["openDirectory", "createDirectory"]
  } else {
    props = ["openFile"]
  }
  const { canceled, filePaths } = await dialog.showOpenDialog({
    properties: props
  });

  if (canceled) {
    return store.get("library-location")
  } else {
    return filePaths[0]
  }
}

function createEntry(event, pth) {
  const full_path = store.get("library-location") + "/" + pth
  fs.mkdir(full_path, (err) => {
    if (err) {
      console.log(err)
    } else {
      console.log("Directory created successfully!")
      return full_path
    }
  })
}

function copyFile(event, src) {
  const dest = store.get("library-location") + "/" + path.basename(src)
  fs.copyFile(src, dest, (err) => {
    if (err) {
      console.log(err)
    } else {
      console.log("File copied successfully!")
      return dest
    }
  })
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

  ipcMain.handle("create-entry", createEntry)
  ipcMain.handle("copy-file", copyFile)

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