const { app, BrowserWindow, Menu } = require("electron")
const path = require("path")
const menu = require("./menu")

function createWindow() {
  const win = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      preload: path.join(__dirname, "preload.js")
    }
  })

  win.loadFile("dist/index.html")
}

app.whenReady().then(() => {
  Menu.setApplicationMenu(Menu.buildFromTemplate(menu))
  createWindow()

  app.on("activate", () => {
    if (BrowserWindow.getAllWindows().length === 0) {
      createWindow()
    }
  })
})

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") {
    app.quit()
  }
})
