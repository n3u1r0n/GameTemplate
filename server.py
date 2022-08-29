from flask import Flask
from flask_socketio import SocketIO


app = Flask('Game')
app.secret_key = 'Game'
socketio = SocketIO(app)


from routes import *


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)