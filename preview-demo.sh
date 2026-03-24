#!/bin/bash

# preview-demo.sh - OpenCurtainCalc 预览演示脚本
# 这个脚本用于展示项目的基本功能和启动方式

echo "=========================================="
echo "🦞 OpenCurtainCalc 预览演示"
echo "=========================================="
echo ""

# 检查Docker是否安装
if ! command -v docker &> /dev/null; then
    echo "⚠️  警告: Docker未安装"
    echo "请先安装Docker: https://docs.docker.com/get-docker/"
    exit 1
fi

# 检查Docker Compose是否安装
if ! command -v docker-compose &> /dev/null; then
    echo "⚠️  警告: Docker Compose未安装"
    echo "请先安装Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ 系统检查完成"
echo ""

echo "📁 项目结构:"
echo "├── backend/          # 后端服务 (FastAPI)"
echo "├── frontend/         # 前端界面 (React)"
echo "├── docker/           # Docker配置文件"
echo "├── scripts/          # 部署脚本"
echo "├── preview.html      # 预览页面 (当前文件)"
echo "└── README.md         # 项目文档"
echo ""

echo "🚀 启动选项:"
echo "1. 启动完整开发环境 (Docker)"
echo "2. 启动后端服务"
echo "3. 启动前端服务"
echo "4. 查看API文档"
echo "5. 查看3D演示"
echo ""

read -p "请选择启动选项 (1-5): " choice

case $choice in
    1)
        echo "正在启动完整开发环境..."
        if [ -f "./scripts/deploy.sh" ]; then
            ./scripts/deploy.sh dev up
        else
            echo "⚠️  未找到部署脚本"
            echo "尝试使用docker-compose..."
            if [ -f "./docker/docker-compose.yml" ]; then
                docker-compose -f ./docker/docker-compose.yml up -d
                echo "✅ 服务已启动"
                echo "前端: http://localhost:3000"
                echo "后端: http://localhost:8000"
            else
                echo "❌ 未找到docker-compose配置文件"
            fi
        fi
        ;;
    2)
        echo "启动后端服务..."
        echo "请确保已安装Python 3.11+和依赖:"
        echo ""
        echo "cd backend"
        echo "pip install poetry"
        echo "poetry install"
        echo "uvicorn app.main:app --reload"
        echo ""
        echo "访问: http://localhost:8000/docs"
        ;;
    3)
        echo "启动前端服务..."
        echo "请确保已安装Node.js 18+和依赖:"
        echo ""
        echo "cd frontend"
        echo "npm install"
        echo "npm run dev"
        echo ""
        echo "访问: http://localhost:3000"
        ;;
    4)
        echo "API文档:"
        echo ""
        echo "1. Swagger UI: http://localhost:8000/docs"
        echo "2. ReDoc: http://localhost:8000/redoc"
        echo ""
        echo "主要API端点:"
        echo "- POST /api/auth/login    # 用户登录"
        echo "- GET  /api/projects      # 项目列表"
        echo "- POST /api/calculations  # 开始计算"
        echo "- GET  /api/materials     # 材料统计"
        ;;
    5)
        echo "3D演示功能:"
        echo ""
        echo "OpenCurtainCalc包含以下3D功能:"
        echo "1. 幕墙结构3D可视化"
        echo "2. 荷载分布3D展示"
        echo "3. 节点构造3D查看"
        echo "4. 施工过程3D模拟"
        echo ""
        echo "技术栈: Three.js + React Three Fiber"
        ;;
    *)
        echo "❌ 无效选项"
        ;;
esac

echo ""
echo "=========================================="
echo "📚 更多信息:"
echo "- GitHub: https://github.com/YIMUYIGUO/open-curtain-calc"
echo "- 文档: 查看README.md文件"
echo "- 问题: 在GitHub Issues中反馈"
echo "=========================================="