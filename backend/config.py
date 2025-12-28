import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecretkey")
    DB_HOST = "localhost"
    DB_NAME = "task_app"
    DB_USER = "postgres"
    DB_PASSWORD = "Akuganteng123#"  
    DB_PORT = "5432"
