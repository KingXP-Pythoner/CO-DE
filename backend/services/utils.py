import uuid

from flask import Flask
from flask_socketio import SocketIO
from mongoengine import connect


def config_mongodb(_app: Flask):
    global db
    if not _app or not isinstance(_app, Flask):
        raise TypeError("Invalid Flask application instance")

    _app.logger.info("Start mongoengine config")
    db = connect(
        db=_app.config["DB_NAME"],
        port=_app.config["DB_PORT"],
        host=_app.config["DB_HOST"],
        uuidRepresentation="standard",
    )
    _app.logger.info(f"End mongoengine config {db}")


def config_socketio(_app: Flask):
    global socketio
    try:
        _app.logger.info("Start websocket config")
        socketio = SocketIO(_app, cors_allowed_origins="*")
        _app.logger.info(f"End websocket config {socketio}")
    except Exception as e:
        _app.logger.error(f"Error during websocket config: {e}")


def generate_invite_token() -> str:
    # Generate unique ID
    uid = uuid.uuid4()
    # Convert to hyphenated string
    hyphenated_hex = "-".join([uid.hex[i : i + 4] for i in range(0, len(uid.hex), 4)])
    return hyphenated_hex
