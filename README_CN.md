# scrcpy GUI

<p align="center">
  <a href="README.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/us.png" height="20"> English</a>
  &nbsp;|&nbsp;
  <a href="README_RU.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ru.png" height="20"> Русский</a>
  &nbsp;|&nbsp;
  <a href="#"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/cn.png" height="20"> <b>中文</b></a>
  &nbsp;|&nbsp;
  <a href="README_KZ.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/kz.png" height="20"> Қазақша</a>
  &nbsp;|&nbsp;
  <a href="README_UA.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/ua.png" height="20"> Українська</a>
  &nbsp;|&nbsp;
  <a href="README_BY.md"><img src="https://raw.githubusercontent.com/stevenrskelton/flag-icon/master/png/75/country-4x3/by.png" height="20"> Беларуская</a>
</p>

[scrcpy](https://github.com/Genymobile/scrcpy) 的图形界面封装 — 轻松镜像和录制 Android 设备屏幕。
专为 QA 测试人员打造。

## 功能特性

- **屏幕镜像** — 在独立窗口中实时显示设备画面
- **屏幕录制** — 录制时实时显示计时器
- **多设备支持** — 从多个已连接设备中选择
- **自动检测设备** — 自动显示已连接设备的型号
- **灵活设置** — 格式（MKV/MP4）、分辨率、码率、帧率、方向、音频、显示触摸
- **自定义图标** — 品牌化 QA 图标，便于识别
- **智能进程管理** — 开始录制时自动关闭镜像，检测 scrcpy 窗口关闭

## 安装

### 方式一 — 安装程序（推荐）

1. 前往 [Releases](../../releases/latest)
2. 下载 `scrcpy-gui-setup-v2.1.0.exe`
3. 运行 → 选择组件 → 安装
4. 桌面将出现快捷方式

> 如果你已安装 scrcpy 或 adb，可以在安装时取消勾选。

### 方式二 — ZIP 压缩包

1. 从 [Releases](../../releases/latest) 下载 `scrcpy-gui-v2.1.0-win64.zip`
2. 解压到任意文件夹
3. 运行 `scrcpy-gui.exe`

### 方式三 — 从源码运行

```bash
pip install customtkinter
python main.py
```

需要 `scrcpy.exe` 位于 `main.py` 同目录或在系统 PATH 中。

## 系统要求

- Windows 10+
- 已开启 USB 调试的 Android 设备
- USB 数据线

### 如何开启 USB 调试

1. **设置** > **关于手机** > 连续点击 **版本号** 7 次
2. **设置** > **开发者选项** > 开启 **USB 调试**
3. 通过 USB 连接手机，在弹窗中允许调试

## 使用方法

1. 通过 USB 连接设备
2. 启动 **scrcpy GUI** — 设备名称自动显示
3. 如果连接了多个设备 — 从下拉列表中选择
4. 点击 **Mirror Screen** — 打开实时镜像窗口
5. 调整设置：格式、分辨率、码率、帧率、方向、音频
6. 点击 **Record** — 镜像关闭，录制开始并显示计时器
7. 点击 **Stop** — 文件保存为 `record_YYYY-MM-DD_HH-MM-SS.mkv`

## 许可证

本项目使用 [scrcpy](https://github.com/Genymobile/scrcpy)（Genymobile / Romain Vimont），基于 [Apache License 2.0](https://github.com/Genymobile/scrcpy/blob/master/LICENSE) 分发。

scrcpy GUI 是独立的封装工具，不修改 scrcpy 本身。
