# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, session, request, \
    copy_current_request_context
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect

async_mode = None

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.event
def connect(auth):
    print('connect ', auth)

@socketio.event
def disconnect():
    print('disconnect ')

@socketio.event
def click_message(sid):
    print('my_click ', sid)
    emit('my_response',"All Ok")

if __name__ == '__main__':
    print_hi('I start server')
    socketio.run(app, port=5000)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
