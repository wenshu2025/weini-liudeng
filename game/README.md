# 为你留灯 · 花开在脚下（本地 v3.4）

双击 `启动游戏.command`（macOS）或 `启动游戏.bat`（Windows）启动本地服务器。已有预览地址为 http://127.0.0.1:8769/ 。

- 原祭坛保留花束、陶罐、烛台和紫色剪纸桌布，缩为2.6米宽；移除四组预置照片及三个支架。前排唯一空相框由露娜放入照片，动作完成前不能跳过，完成后读档保留。
- 但丁使用用户提供的 `dante-walk-tripo.glb`，包含四足骨骼和2.58秒行走。广场引路、停步等人、陪伴过桥；点击“但丁”或靠近按E互动。站姿和轻微头部回应由程序控制，没有独立的嗅闻、坐下或完整抚摸动画。小狗位置随旅程保存。
- 花桥按实际步点绽放花瓣和暖光，桥头结界可摊掌或点击触碰。
- 桥外播放《鸟之诗（八音盒版）》，桥上播放《Remember Me》；暂停、静音与读档续播。
- 两侧方块建筑占位已撤去，保留双世界远景和用户现有场景。

操作：WASD/方向键移动、拖动画面环顾、E互动、J记忆册、V切换视角；点击地标自动走近。摄像头手势需主动开启，按钮可完成全部流程。

普通存档兼容。新增测试只使用独立测试键，不覆盖普通游戏进度。真人摄像头识别尚未实测。

检查：`node test-restored-assets.mjs`、`node test-photo-state.mjs`、`node test-story.mjs`、`node test-v2.mjs`、`node test-journey.mjs`、`node test-audio-journey.mjs`、`node test-gestures.mjs`。

原祭坛和狗的原始文件不修改。衍生祭坛制作脚本位于工作区 `edit/altar-remembrance/prepare_assets.py`。运行素材校验见 `asset-manifest-v3.json`，旧模型来源见 `asset-manifest-v2.json`。v3.4 已部署到 https://weini-liudeng.wenshu2025.workers.dev ，发布记录位于 deploy/cloudflare/deployment.json。
