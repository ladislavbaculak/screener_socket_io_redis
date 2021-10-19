from aiohttp import web
import socketio

sio = socketio.AsyncServer()  # instance of socket io server
app = web.Application()
sio.attach(app)


@sio.event
async def connect(sid, environ):
    '''When client connects, print his SID.'''
    print(sid, 'Connected')


@sio.event
async def disconnect(sid):
    '''When client disconnect, print his SID.'''
    print(sid, 'Disconnected from')
    await sio.disconnect(sid)


@sio.event
async def message(sid, message):
    '''Message send to the room by client.'''
    await sio.emit('message_in_room', {'msg': message, 'sid': sid},
                   to='Redis_Room')


@sio.event
async def rooms(sid, data_rooms):
    '''Connect client to the room and emit message to client about it.'''
    sio.enter_room(sid, 'Redis_Room')
    await sio.emit('status_room', {'status': f'''You Are Connected To:
                                  {data_rooms["room"]} Room.'''}, to=sid)


def main():
    web.run_app(app)


if __name__ == '__main__':
    main()
