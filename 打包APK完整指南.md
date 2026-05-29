# 📱 打包成 APK 完整指南

## 🎯 方案一：PWA（最简单，推荐先试！）

### 什么是PWA？
- ✅ 不需要安装Android Studio
- ✅ 可以直接添加到手机桌面，像原生应用一样
- ✅ 图标、启动画面都有！

### 步骤：

1. **先正常打包项目**
   ```bash
   npm run build
   ```

2. **把 dist 文件夹部署到网上**
   - 推荐用 GitHub Pages 或 Vercel（免费）
   - 或者用任何静态网站托管

3. **用手机访问网站**
   - 在手机Chrome浏览器中打开
   - 点击右上角菜单 -> "添加到主屏幕"
   - 完成！桌面会出现应用图标！

---

## 🚀 方案二：真正的 APK 文件（推荐）

使用 **Capacitor** 把项目打包成APK！

### 第一步：准备工作

1. **安装 Node.js**（你已经有了）
2. **安装 Android Studio**
   - 下载：https://developer.android.com/studio
   - 安装后打开，安装 Android SDK（默认会提示）

### 第二步：配置项目

1. **安装 Capacitor**
   在项目目录打开终端，运行：
   ```bash
   npm install @capacitor/core @capacitor/cli @capacitor/android -D
   ```

2. **初始化 Capacitor**
   ```bash
   npx cap init "校园搭子" "com.campusvibe.app"
   ```

3. **添加 Android 平台**
   ```bash
   npx cap add android
   ```

4. **修改 capacitor.config.json**
   打开文件，确保如下配置：
   ```json
   {
     "appId": "com.campusvibe.app",
     "appName": "校园搭子",
     "webDir": "dist",
     "server": {
       "androidScheme": "https"
     }
   }
   ```

### 第三步：打包流程

1. **先构建前端**
   ```bash
   npm run build
   ```

2. **同步到 Android 项目**
   ```bash
   npx cap sync
   ```

3. **打开 Android Studio**
   ```bash
   npx cap open android
   ```

4. **在 Android Studio 中构建 APK**
   - 等待 Gradle 同步完成
   - 点击菜单：Build -> Build Bundle(s) / APK(s) -> Build APK(s)
   - 构建完成后会弹出提示，点击 "locate" 就能找到 APK 文件！

### APK 位置：
```
android/app/build/outputs/apk/debug/app-debug.apk
```

这个 APK 就可以直接发给朋友安装了！

---

## 🎁 方案三：桌面应用（Windows/Mac）

使用 Electron 打包成桌面端！

### 快速开始：

1. **安装 Electron Builder**
   ```bash
   npm install -D electron electron-builder vite-plugin-electron
   ```

2. **创建 electron/main.js**
   ```javascript
   const { app, BrowserWindow } = require('electron')
   const path = require('path')
   
   function createWindow() {
     const win = new BrowserWindow({
       width: 430,
       height: 900,
       webPreferences: {
         nodeIntegration: true
       }
     })
     
     if (app.isPackaged) {
       win.loadFile('dist/index.html')
     } else {
       win.loadURL('http://localhost:5173')
     }
   }
   
   app.whenReady().then(createWindow)
   ```

3. **在 package.json 添加**
   ```json
   {
     "main": "electron/main.js",
     "scripts": {
       "electron:dev": "electron .",
       "electron:build": "npm run build && electron-builder"
     }
   }
   ```

4. **打包**
   ```bash
   npm run electron:build
   ```

会在 `dist` 文件夹生成 .exe (Windows) 或 .dmg (Mac) 文件！

---

## 📌 推荐操作顺序

1. **先用 PWA 测试效果**（最简单）
2. **满意后再打 APK**（正式分发）
3. **需要桌面端再用 Electron**

---

## 💡 常见问题

**Q: APK 安装提示"未知来源"？**
A: 在手机设置里允许安装未知来源应用就行

**Q: 想发布到应用商店？**
A: 需要生成签名密钥，然后构建 Release 版本，过程稍微复杂一点，需要可以再问我

**Q: 后端API怎么办？**
A: 目前后端是本地的，如果要在 APK 里用，需要把后端部署到服务器上
