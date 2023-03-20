//Dimonti was here
<<<<<<< HEAD



//TEST

//LastCommit
=======
//Dimonti is gone
>>>>>>> c9e696b96b3644c74ba561d2238e6e724af6b1bb
let ws = new WebSocket('ws://localhost:8000/ws');
let infoDisplay = document.getElementById('info')
let currentPlayerDisplay = document.getElementById('current-player')
let infoPlayer = document.getElementById('player')
let player = null
let currentPlayer = null
let checks = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [6, 4, 2],
]
let gameOver = false
let swaper = {
    'X': 'O',
    'O': 'X'
}

function checkCell(cell) {
    if (cell.innerHTML === '*' && player === currentPlayer) {
        return true
    }
    return false
}

function cellClick(id) {
    if (gameOver) { return }

    cell = document.getElementById(id)

    if (checkCell(cell)) { ws.send(JSON.stringify({ player: player, cell: id })) }

    else { infoDisplay.innerHTML = "Выберите другую клетку! Или ждите своего хода!" }
}

function updateCell(id, sign) {
    cell = document.getElementById(id)
    cell.innerHTML = sign
}

function updateInfo(message) {
    infoDisplay.innerHTML = message
}

function toggleplayer() {
    currentPlayer = swaper[currentPlayer]
    console.log("Переключился на игрока ", player, currentPlayer)
    if (player === currentPlayer) {
        infoDisplay.innerHTML = "Ваш ход"
        currentPlayerDisplay.innerHTML = player
    } else {
        infoDisplay.innerHTML = "Ход противника"
        currentPlayerDisplay.innerHTML = swaper[player]
    }
}

function highlightAll(){
    for (let i = 1; i < 10; i++){
        document.getElementById(i).style.backgroundColor = 'gray'
    }
}

function highlightRow() {
    let cells = []
    for (let i = 1; i < 10; i++) {
        cells.push(document.getElementById(i))
    }
    checks.forEach((row) => {
        console.log(row)
        if (cells[row[0]].innerHTML === cells[row[1]].innerHTML && cells[row[0]].innerHTML === cells[row[2]].innerHTML && cells[row[0]].innerHTML !== "*"){
            console.log(cells[row[0]].innerHTML, cells[row[1]].innerHTML, cells[row[2]].innerHTML)
            cells[row[0]].style.backgroundColor = 'red'
            cells[row[1]].style.backgroundColor = 'red'
            cells[row[2]].style.backgroundColor = 'red'
            return
        }
    })
}

ws.onmessage = function(e) {
    let response = JSON.parse(e.data)
    console.log("On message", response)
    if (response.init) {
        infoDisplay.innerHTML = "Вы играете за: "+ response.player + ". " + response.message
        infoPlayer.innerHTML = response.player
        if (response.message !== "В ожидании другого игрока!") {
            player = response.player
        }
        currentPlayer = player
        currentPlayerDisplay.innerHTML = player
    } else {
        if (response.message === 'ход') {
            updateCell(response.cell, response.player)
            toggleplayer()
        } else if (response.message === 'ничья') {
            updateInfo("Это ничья!")
            updateCell(response.cell, response.player)
            highlightAll()
            ws.close(1000)
        } else if (response.message === 'выиграл') {
            updateInfo("Игрок " + response.player + " выиграл!")
            updateCell(response.cell, response.player)
            highlightRow()
            ws.close(1000)
        } else if (response.player === player && response.message === 'Выберите другую клетку') {
            updateInfo("Ход не правильный")
        } else {
            console.log(response)
        }
    }
}

ws.onclose = function (e) {
    if (e.code === 4000) {
        infoDisplay.innerHTML = "Не осталось мест"
    } else if (e.code !== 1000) {
        infoDisplay.innerHTML = "Ошибка"
    }
    gameOver = true
}

