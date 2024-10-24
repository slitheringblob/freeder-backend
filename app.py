from flask import Flask
from backend.feed import feed_router

app = Flask(__name__)
app.register_blueprint(feed_router)
