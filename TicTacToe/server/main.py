from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List
import json

app = FastAPI()


def init_board():
    return [
        None, None, None,
        None, None, None,
        None, None, None,
    ]


board = init_board()


def is_draw():
    global board
    for cell in board:
        if not cell:
            return False

    board = init_board()
    return True


def if_won():
    global board
    if board[0] == board[1] == board[2] != None or \
            board[3] == board[4] == board[5] != None or \
            board[6] == board[7] == board[8] != None or \
            board[0] == board[3] == board[6] != None or \
            board[1] == board[4] == board[7] != None or \
            board[2] == board[5] == board[8] != None or \
            board[0] == board[4] == board[8] != None or \
            board[6] == board[4] == board[2] != None:
        board = init_board()
        return True
    return False


async def update_board(manager, data):
    ind = int(data['cell']) - 1
    data['init'] = False
    if not board[ind]:
        board[ind] = data['player']
        if is_draw():
            data['message'] = "ничья"
        elif if_won():
            data['message'] = "выиграл"
        else:
            data['message'] = "ход"
    else:
        data['message'] = "Выберите другую клетку"
    await manager.broadcast(data)
    if data['message'] in ['ничья', 'выиграл']:
        manager.connections = []


class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        if len(self.connections) > 2:
            await websocket.accept()
            await websocket.close(4000)
        else:
            await websocket.accept()
            self.connections.append(websocket)
            if len(self.connections) == 1:
                await websocket.send_json({
                    'init': True,
                    'player': 'X',
                    'message': 'В ожидании другого игрока!',
                })
            else:
                await websocket.send_json({
                    'init': True,
                    'player': 'O',
                    'message': '',
                })

                await self.connections[0].send_json({
                    'init': True,
                    'player': 'X',
                    'message': 'Ваш ход',
                })
        self.connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.connections.remove(websocket)

    async def broadcast(self, data: str):
        for connection in self.connections:
            await connection.send_json(data)


manager = ConnectionManager()


@app.websocket("/ws")  # Ождание протокола
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)  # принимает соединение
    try:
        while True:
            data = await websocket.receive_text()
            data = json.loads(data)
            await update_board(manager, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except:
        pass
