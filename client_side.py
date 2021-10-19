import asyncio
import socketio

sio = socketio.AsyncClient()


@sio.event
async def message_in_room(message):
    '''Print a message sended into the room by connected client.'''
    print(' ')
    print(f'{message["msg"]}')


@sio.event
async def connect():
    '''Connect to the selected room and print "connection established" message
    to client.'''
    print('connection established')
    await sio.emit('rooms', {'room': 'Redis_Room'})


@sio.event
async def disconnect():
    '''Disconnect message when server disconnect client.'''
    print('disconnected from server')


@sio.event
async def status_room(status):
    '''Print a message "You are connected to: X room".'''
    print(status['status'])


async def main():
    await sio.connect('http://localhost:8080')
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(main())
