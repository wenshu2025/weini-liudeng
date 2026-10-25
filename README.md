# 为你留灯 · The Light We Leave

一款关于记忆、陪伴与继续生活的 3D 叙事游戏。玩家作为桥灯学徒，系好旧鞋、调一份点心、折一朵纸花，陪伊莲娜和小狗但丁走过花瓣桥，让露娜把奶奶的照片放回祭坛。

**在线试玩：** https://weini-liudeng.wenshu2025.workers.dev

## 本地运行

需要 Python 3.9+；运行检查还需要 Node.js 22+。游戏本身使用原生 ES Modules 和本地 Three.js，无需前端编译。

```bash
git clone https://github.com/wenshu2025/weini-liudeng.git
cd weini-liudeng
python3 scripts/fetch_assets.py
python3 -m http.server 8769 --bind 127.0.0.1 --directory game
```

浏览器打开 http://127.0.0.1:8769/ 。也可在素材恢复后双击 `game/启动游戏.command` 或 `game/启动游戏.bat`。

运行素材约 167 MB，独立于源码版本管理。下载脚本从已发布站点恢复素材，并按 `assets-manifest.json` 校验 SHA-256。完整素材备份见本仓库 **Releases → v3.4 → weini-liudeng-assets-v3.4.zip**。私有附件需要登录 GitHub 下载，可离线恢复：

```bash
python3 scripts/fetch_assets.py --archive /path/to/weini-liudeng-assets-v3.4.zip
```

## 操作与功能

- WASD / 方向键或手机屏幕方向键移动；点击地标可自动走近。
- E 互动、J 记忆册、V 切换视角；拖动画面环顾。
- 三件旧物支持拖动、选择甜度、折花和摊掌点灯，也可全程使用按钮。
- 18 个场景、道具、人物模型；原装饰祭坛只有一个可放照片的空相框。
- 但丁使用四足行走循环，支持引路、等待、过桥同行和靠近互动。
- 按步点触发花瓣与暖光，穿越桥头结界；桥外八音盒与桥上摇篮曲切换。
- 摄像头手势需主动开启，识别在设备本地进行；不采集麦克风、不上传画面。
- 旅程、照片放置与小狗位置保存在当前浏览器。

## 检查

```bash
npm test
npm run test:assets
```

前者检查剧情、存档、照片状态、步点、音频与手势逻辑；后者检查素材模型结构，需先恢复素材。

## Cloudflare 发布

```bash
npm run build
npx wrangler@4.151.3 login
npm run deploy
```

配置位于 `deploy/cloudflare/wrangler.jsonc`，发布目标为原 Worker `weini-liudeng`。仓库不包含登录信息或 API 密钥，不配置自动部署。

## 目录

- `game/`：游戏源代码、测试和启动器。
- `scripts/`：素材下载、离线恢复和部署构建。
- `assets-manifest.json`：运行素材及原祭坛编辑源的校验清单。
- `edit/altar-remembrance/`：保留原祭坛装饰、移除旧照片组件的制作脚本。
- `deploy/cloudflare/`：部署配置与发布记录。

模型与音乐为项目提供的素材，归各自权利方所有；第三方运行库随素材附件保留其原始说明与许可证。本仓库未授予对所有素材的开源许可。
