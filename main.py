# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, session, request, \
    copy_current_request_context, logging
from flask_socketio import SocketIO, emit, join_room, leave_room, \
    close_room, rooms, disconnect
from threading import Thread, Event
import  time
import logging

async_mode = None

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app,logger=True)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)
    #return "Hello, World!"
@app.route('/contact')
def contact():
    return render_template('contact.html', async_mode=socketio.async_mode)
@app.route('/send')
def send():
    return render_template('send.html', async_mode=socketio.async_mode)
    #return "Hello, World!"

@socketio.event
def connect(auth):
    print('connect ', auth)

@socketio.event
def disconnect():
    print('disconnect ')

@socketio.event
def click_message(sid):
    global counter
    print('my_click ', sid)
    emit('my_response',"All Ok = "+str(counter))
    counter += 1
#------------------------------------------------------------
def server():
    socketio.run(app, port=5000)


counter= 0
counter_2=0
def background_work():
    global counter
    i=0
    while True:
        mes = "Counter = "+str(counter) + " second"

        print(mes)
        socketio.emit('my_response', mes)
        time.sleep(1)
        counter += 1
        i = 0
        #time.sleep(2)

# def background_work_2():
#     global counter_2
#     while True:
#         mes = "Counter_2 = "+str(counter_2)
#         print(mes)
#         #socketio.emit('my_response', mes)
#         #time.sleep(1)
#         counter_2 += 1
#         time.sleep(4)


#------------------------------------------------
if __name__ == '__main__':
    print_hi('I start server')

    #
    #counter_thread=Thread(target=background_work)
    #counter_thread_2 = Thread(target=background_work_2)
    #counter_thread.start()
    #counter_thread_2.start()

   # socketio.run(app, port=5000)
    server_thread = Thread(target=server)
    server_thread.start()

    # background_thread = Thread(target=background_work)
    # background_thread.start()
    background_work()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
