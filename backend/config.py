import os

class Config:
    FLASK_ENV='app.py'

class DevelopmentConfig(Config):
    FLASK_ENV='development'

class ProductionConfig(Config):
    FLASK_RUN_HOST='0.0.0.0'

if os.environ['ENV'] == 'production':
    config = ProductionConfig()
elif os.environ['ENV'] == 'development':
    config = DevelopmentConfig()
else:
    config = Config()