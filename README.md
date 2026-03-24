# OpenCurtainCalc - 开源幕墙计算系统

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![React](https://img.shields.io/badge/react-18+-61dafb.svg)
![Docker](https://img.shields.io/badge/docker-ready-2496ed.svg)

OpenCurtainCalc 是一个功能全面的开源幕墙计算系统，旨在替代商业软件如豪沃克幕墙计算软件。系统提供完整的幕墙设计、计算、分析和报告生成功能。

## ✨ 特性

### 🏗️ 核心功能
- **结构计算**: 立柱、横梁、连接件等结构计算
- **荷载分析**: 风荷载、地震荷载、温度荷载等
- **材料统计**: 自动材料用量计算和成本估算
- **节点设计**: 连接节点设计和验算
- **计算书生成**: 自动生成符合国标的计算书

### 🚀 增强功能（优于豪沃克）
- **BIM集成**: 支持Revit、Rhino、SketchUp文件导入
- **参数化设计**: Grasshopper集成，支持参数优化
- **云协同**: 多人实时协作设计
- **AI辅助**: 智能优化建议和异常检测
- **移动端支持**: 手机/平板查看和简单计算
- **3D可视化**: 交互式3D模型展示
- **API开放**: 完整的REST API接口

### 📊 技术特点
- **现代化架构**: 前后端分离，微服务架构
- **高性能**: 异步计算引擎，支持大规模计算
- **可扩展**: 插件化架构，易于功能扩展
- **跨平台**: 支持Windows、macOS、Linux
- **容器化**: Docker一键部署

## 📋 系统架构

```
┌─────────────────────────────────────────────────────────┐
│                    前端界面 (React)                      │
├─────────────────────────────────────────────────────────┤
│                    API网关 (FastAPI)                    │
├─────────────────────────────────────────────────────────┤
│   计算引擎    │   文件处理   │   BIM集成   │    AI服务   │
├─────────────────────────────────────────────────────────┤
│                    消息队列 (Redis)                      │
├─────────────────────────────────────────────────────────┤
│                    数据库 (PostgreSQL)                   │
└─────────────────────────────────────────────────────────┘
```

## 🛠️ 技术栈

### 后端
- **Python 3.11+**: 主要编程语言
- **FastAPI**: 高性能Web框架
- **PostgreSQL**: 主数据库
- **Redis**: 缓存和消息队列
- **Celery**: 异步任务队列
- **SQLAlchemy**: ORM框架
- **Pydantic**: 数据验证
- **PythonOCC**: CAD内核集成

### 前端
- **React 18+**: UI框架
- **TypeScript**: 类型安全
- **Material-UI**: UI组件库
- **Three.js**: 3D可视化
- **React Query**: 数据管理
- **Zustand**: 状态管理
- **Vite**: 构建工具

### 基础设施
- **Docker**: 容器化
- **Docker Compose**: 服务编排
- **Nginx**: 反向代理
- **GitHub Actions**: CI/CD
- **Sentry**: 错误监控
- **Prometheus**: 监控指标
- **Grafana**: 监控面板

## 🚀 快速开始

### 前提条件
- Docker 20.10+
- Docker Compose 2.0+
- Git

### 一键部署

```bash
# 克隆项目
git clone https://github.com/your-org/open-curtain-calc.git
cd open-curtain-calc

# 启动开发环境
./scripts/deploy.sh dev up

# 访问应用
# 前端: http://localhost:3000
# 后端API: http://localhost:8000
# API文档: http://localhost:8000/docs
```

### 手动安装

#### 1. 后端设置

```bash
cd backend

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate  # Windows

# 安装依赖
pip install poetry
poetry install

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件设置数据库等配置

# 初始化数据库
alembic upgrade head

# 启动服务
uvicorn app.main:app --reload
```

#### 2. 前端设置

```bash
cd frontend

# 安装依赖
npm install

# 启动开发服务器
npm run dev
```

## 📁 项目结构

```
open-curtain-calc/
├── backend/                    # 后端服务
│   ├── app/                   # 应用代码
│   │   ├── api/              # API接口
│   │   ├── core/             # 核心模块
│   │   ├── models/           # 数据模型
│   │   ├── schemas/          # 数据验证
│   │   └── services/         # 业务服务
│   ├── calc_engine/          # 计算引擎
│   │   ├── structural/       # 结构计算
│   │   ├── material/         # 材料计算
│   │   ├── wind/             # 风荷载计算
│   │   └── seismic/          # 地震计算
│   ├── cad_integration/      # CAD集成
│   └── database/             # 数据库配置
├── frontend/                  # 前端界面
│   ├── src/
│   │   ├── components/       # 组件
│   │   ├── pages/            # 页面
│   │   ├── services/         # API服务
│   │   └── utils/            # 工具函数
│   └── public/
├── docker/                    # Docker配置
├── scripts/                   # 部署脚本
├── docs/                      # 文档
└── tests/                     # 测试
```

## 🔧 配置说明

### 环境变量

创建 `.env` 文件：

```env
# 应用配置
APP_NAME=OpenCurtainCalc
APP_VERSION=0.1.0
DEBUG=true
SECRET_KEY=your-secret-key-change-in-production

# 数据库
DATABASE_URL=postgresql://postgres:password@localhost:5432/curtain_calc

# Redis
REDIS_URL=redis://localhost:6379/0

# 文件上传
UPLOAD_DIR=./uploads
MAX_UPLOAD_SIZE=104857600  # 100MB

# CAD软件路径（可选）
AUTOCAD_PATH=/path/to/autocad
RHINO_PATH=/path/to/rhino
```

### 数据库迁移

```bash
# 创建迁移
alembic revision --autogenerate -m "描述"

# 应用迁移
alembic upgrade head

# 回滚迁移
alembic downgrade -1
```

## 📚 API文档

启动服务后访问：
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## 🧪 测试

```bash
# 运行后端测试
cd backend
pytest tests/ -v

# 运行前端测试
cd frontend
npm test

# 运行端到端测试
npm run test:e2e
```

## 🐳 Docker部署

### 开发环境

```bash
# 启动所有服务
docker-compose -f docker/docker-compose.yml up -d

# 查看日志
docker-compose logs -f

# 停止服务
docker-compose down
```

### 生产环境

```bash
# 构建生产镜像
docker-compose -f docker/docker-compose.prod.yml build

# 启动生产服务
docker-compose -f docker/docker-compose.prod.yml up -d
```

## 📈 监控和运维

### 健康检查
- 应用健康: `GET /health`
- 数据库健康: `GET /health/db`
- Redis健康: `GET /health/redis`

### 监控面板
- Flower (Celery监控): http://localhost:5555
- pgAdmin (数据库管理): http://localhost:5050
- Grafana (系统监控): http://localhost:3001

### 日志查看
```bash
# 查看所有服务日志
docker-compose logs -f

# 查看特定服务日志
docker-compose logs -f backend

# 实时日志
docker-compose logs -f --tail=100
```

## 🔄 开发工作流

### 分支策略
- `main`: 生产分支
- `develop`: 开发分支
- `feature/*`: 功能分支
- `bugfix/*`: 修复分支
- `release/*`: 发布分支

### 提交规范
```
type(scope): subject

body

footer
```

类型说明：
- `feat`: 新功能
- `fix`: 修复bug
- `docs`: 文档更新
- `style`: 代码格式
- `refactor`: 重构
- `test`: 测试
- `chore`: 构建/工具

## 🤝 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'feat: Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 创建 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 📞 支持

- 📖 [文档](https://docs.curtaincalc.com)
- 🐛 [问题反馈](https://github.com/your-org/open-curtain-calc/issues)
- 💬 [讨论区](https://github.com/your-org/open-curtain-calc/discussions)
- 📧 邮箱: support@curtaincalc.com

## 🙏 致谢

感谢以下开源项目的贡献：
- [FastAPI](https://fastapi.tiangolo.com/)
- [React](https://reactjs.org/)
- [Material-UI](https://mui.com/)
- [Three.js](https://threejs.org/)
- [Docker](https://www.docker.com/)

## 🏆 对比豪沃克

| 功能 | 豪沃克 | OpenCurtainCalc |
|------|--------|-----------------|
| 价格 | 商业软件（9800元起） | 开源免费 |
| 源代码 | 闭源 | 完全开源 |
| 定制化 | 有限 | 高度可定制 |
| 云协同 | 不支持 | 支持 |
| 移动端 | 不支持 | 支持 |
| AI辅助 | 不支持 | 支持 |
| API开放 | 不支持 | 完整API |
| 社区支持 | 有限 | 活跃社区 |
| 部署方式 | Windows桌面 | 跨平台，支持云部署 |

## 📊 路线图

### v0.1.0 (当前)
- [x] 基础项目结构
- [x] 用户认证系统
- [x] 项目管理
- [x] 基础计算引擎
- [x] Docker部署

### v0.2.0 (计划中)
- [ ] 完整计算模块
- [ ] 3D可视化
- [ ] CAD文件导入
- [ ] 计算书生成

### v0.3.0
- [ ] BIM集成
- [ ] 参数化设计
- [ ] 云协同功能
- [ ] 移动端应用

### v1.0.0
- [ ] AI辅助设计
- [ ] 施工模拟
- [ ] 企业级功能
- [ ] 完整文档

---

**OpenCurtainCalc - 让幕墙设计更智能、更高效**

⭐ 如果这个项目对你有帮助，请给我们一个Star！