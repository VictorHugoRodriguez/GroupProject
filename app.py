from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy

# Init Flask app
app = Flask(__name__)
# SQLite db configure
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/sensorLogs.db'
db = SQLAlchemy(app)
# Init socket instance with app
socketio = SocketIO(app)

# DB model class
class SimpleLogDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float, nullable=False)
    level = db.Column(db.Float, nullable=False)
    flow = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Log %f, %f, %f>' % (self.temp, self.level, self.flow)

# Class object to define how a single log we recieve from LABVIEW should look like
class SimpleLog:
    temp = 0.0
    level = 0.0
    flow = 0.0
    def __init__(self, temp, level, flow):
        self.temp = temp
        self.level = level
        self.flow = flow
# Array of SimpleLogs
logs = []

# Serve index.html
@app.route('/')
def index():
    """ Serve Index HTML """
    return render_template( 'index.html' )

# Socket log event, sent from client, caught here
@socketio.on( 'log' )
def on_create(data):
    """ Create a connection channel """
    logs.append(
        SimpleLog(data['temp'], data['level'], data['flow'])
        )
    tmp = SimpleLogDB(
        temp = data['temp'],
        level = data['level'],
        flow = data['flow']
    )
    db.session.add(tmp)
    db.session.commit()
    emit('success', data)

if __name__ == '__main__':
    socketio.run(app, debug=True)