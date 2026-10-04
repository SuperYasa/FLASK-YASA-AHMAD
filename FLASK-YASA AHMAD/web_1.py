from flask import Flask
from a2wsgi import WSGIMiddleware

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "<h1>Hello Flask</h1>"

# Wrap Flask agar kompatibel dengan Uvicorn/ASGI
app = WSGIMiddleware(flask_app)