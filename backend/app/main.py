from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html
from contextlib import asynccontextmanager
import logging
from pathlib import Path

from app.core.config import settings
from app.core.database import engine, get_db, create_tables
from app.models import Base

# 配置日志
logging.basicConfig(
    level=logging.DEBUG if settings.DEBUG else logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    应用生命周期管理
    """
    logger.info("🚀 启动 OpenCurtainCalc 应用")
    
    # 启动时执行
    try:
        # 创建数据库表（仅开发环境）
        if settings.DEBUG:
            logger.info("🔧 创建数据库表...")
            Base.metadata.create_all(bind=engine)
        
        # 创建必要目录
        settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"📁 上传目录: {settings.UPLOAD_DIR.absolute()}")
        logger.info(f"🌐 允许的源: {settings.ALLOWED_ORIGINS}")
        
    except Exception as e:
        logger.error(f"❌ 启动失败: {e}")
        raise
    
    yield  # 应用运行期间
    
    # 关闭时执行
    logger.info("🛑 关闭 OpenCurtainCalc 应用")
    # 清理资源


# 创建FastAPI应用
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="开源幕墙计算系统 - 豪沃克平替软件",
    docs_url=None,  # 自定义文档
    redoc_url="/redoc",
    lifespan=lifespan,
)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 挂载静态文件
uploads_path = Path(settings.UPLOAD_DIR)
app.mount("/uploads", StaticFiles(directory=uploads_path), name="uploads")

# 自定义Swagger UI
@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=f"{settings.APP_NAME} - Swagger UI",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css",
    )


# 健康检查
@app.get("/health")
async def health_check():
    """
    健康检查端点
    """
    return {
        "status": "healthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "timestamp": datetime.utcnow().isoformat(),
    }


# 根路径
@app.get("/")
async def root():
    """
    根路径
    """
    return {
        "message": f"欢迎使用 {settings.APP_NAME} v{settings.APP_VERSION}",
        "docs": "/docs",
        "redoc": "/redoc",
        "health": "/health",
        "api": {
            "v1": "/api/v1",
        }
    }


# API路由
from app.api import users, projects, calculations, materials, files, auth

# 注册API路由
api_v1_prefix = "/api/v1"

# 认证相关
app.include_router(auth.router, prefix=api_v1_prefix, tags=["认证"])

# 用户相关
app.include_router(users.router, prefix=api_v1_prefix, tags=["用户"])

# 项目相关
app.include_router(projects.router, prefix=api_v1_prefix, tags=["项目"])

# 计算相关
app.include_router(calculations.router, prefix=api_v1_prefix, tags=["计算"])

# 材料相关
app.include_router(materials.router, prefix=api_v1_prefix, tags=["材料"])

# 文件相关
app.include_router(files.router, prefix=api_v1_prefix, tags=["文件"])


# 错误处理
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.error(f"HTTP错误: {exc.status_code} - {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"error": exc.detail},
    )


@app.exception_handler(Exception)
async def general_exception_handler(request, exc):
    logger.error(f"未处理异常: {exc}", exc_info=True)
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"error": "内部服务器错误"},
    )


# 导入必要的模块
from datetime import datetime
from fastapi.responses import JSONResponse

if __name__ == "__main__":
    import uvicorn
    
    logger.info(f"🚀 启动服务器: http://localhost:8000")
    logger.info(f"📚 API文档: http://localhost:8000/docs")
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info" if settings.DEBUG else "warning",
    )