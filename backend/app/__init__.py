from flask import Flask
from config import config
from app.apis import blueprint as api

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(api, url_prefix="/")