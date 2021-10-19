import asyncio
import socketio
from services.redis import redis_m

sio = socketio.AsyncClient()  # instance of socket io server


@sio.event
async def send_message(message):
    '''Send message to the room from connected client.'''
    print(f'Sending: {message}')
    await sio.send(message)


@sio.event
async def connect():
    '''Connect to the selected room and print "connection established" message
    to client.'''
    print('connection established')
    await sio.emit('rooms', {'room': 'Redis_Room'})


@sio.event
async def disconnect():
    '''Disconnect message when server disconnect client'''
    print('disconnected from server')


async def main():
    await sio.connect('http://localhost:8080')
    while True:
        try:
            await send_message(redis_m.decode())
            await sio.sleep(60)
        except KeyboardInterrupt:
            break
    await sio.wait()


if __name__ == '__main__':
    asyncio.run(main())
