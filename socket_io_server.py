import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

def start_server():
    print('Starting server')
    eventlet.wsgi.server(eventlet.listen(('', 8008)), app)


if __name__ == '__main__':
    start_server()
