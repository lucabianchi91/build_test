import socketio
import eventlet
import threading
from socket_io_server import start_server


if __name__ == '__main__':
    t = threading.Thread(target=start_server)
    t.start()
    sio = socketio.Client()
    sio.connect('http://localhost:8008')
    print('Hello world')

