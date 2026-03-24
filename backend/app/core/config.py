import os
from pathlib import Path
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """应用配置"""
    
    # 基础配置
    APP_NAME: str = "OpenCurtainCalc"
    APP_VERSION: str = "0.1.0"
    DEBUG: bool = Field(default=False, env="DEBUG")
    
    # 安全配置
    SECRET_KEY: str = Field(
        default="your-secret-key-change-in-production",
        env="SECRET_KEY"
    )
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # 数据库配置
    DATABASE_URL: str = Field(
        default="postgresql://postgres:password@localhost:5432/curtain_calc",
        env="DATABASE_URL"
    )
    
    # Redis配置
    REDIS_URL: str = Field(
        default="redis://localhost:6379/0",
        env="REDIS_URL"
    )
    
    # CORS配置
    ALLOWED_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    # 文件存储
    UPLOAD_DIR: Path = Field(
        default=Path("./uploads"),
        env="UPLOAD_DIR"
    )
    MAX_UPLOAD_SIZE: int = 100 * 1024 * 1024  # 100MB
    
    # CAD配置
    AUTOCAD_PATH: Optional[str] = Field(
        default=None,
        env="AUTOCAD_PATH"
    )
    RHINO_PATH: Optional[str] = Field(
        default=None,
        env="RHINO_PATH"
    )
    
    # 计算配置
    DEFAULT_SAFETY_FACTOR: float = 1.4
    DEFAULT_MATERIAL_PROPERTIES: dict = {
        "aluminum_6063_t5": {
            "name": "铝合金 6063-T5",
            "density": 2700,  # kg/m³
            "elastic_modulus": 70e9,  # Pa
            "tensile_strength": 160e6,  # Pa
            "compressive_strength": 160e6,  # Pa
            "shear_strength": 100e6,  # Pa
            "thermal_expansion": 23e-6,  # 1/°C
        },
        "steel_q235": {
            "name": "钢材 Q235",
            "density": 7850,  # kg/m³
            "elastic_modulus": 210e9,  # Pa
            "tensile_strength": 235e6,  # Pa
            "compressive_strength": 235e6,  # Pa
            "shear_strength": 135e6,  # Pa
            "thermal_expansion": 12e-6,  # 1/°C
        },
        "glass_tempered": {
            "name": "钢化玻璃",
            "density": 2500,  # kg/m³
            "elastic_modulus": 72e9,  # Pa
            "tensile_strength": 90e6,  # Pa
            "compressive_strength": 700e6,  # Pa
            "thermal_expansion": 9e-6,  # 1/°C
        }
    }
    
    # 规范配置
    STANDARD_CODES: dict = {
        "GB50009": "建筑结构荷载规范",
        "GB50017": "钢结构设计标准",
        "GB50010": "混凝土结构设计规范",
        "GBT21086": "建筑幕墙",
        "JGJ102": "玻璃幕墙工程技术规范",
        "JGJ133": "金属与石材幕墙工程技术规范",
    }
    
    class Config:
        env_file = ".env"
        case_sensitive = True


# 创建配置实例
settings = Settings()

# 确保上传目录存在
settings.UPLOAD_DIR.mkdir(parents=True, exist_ok=True)