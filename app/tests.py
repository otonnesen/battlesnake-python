from board import board
data = {
  "width": 13,
  "height": 18,
  "id": 2256,
  "turn": 2,
  "snakes": {
    "data": [
      {
        "id": "64f03f9f-c332-4330-8a1e-8342c8d887c7",
        "health": 98,
        "length": 3,
        "taunt": "Boop the snoot!",
        "name": "LUL",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 0,
              "y": 9
            },
            {
              "object": "point",
              "x": 1,
              "y": 9
            },
            {
              "object": "point",
              "x": 2,
              "y": 9
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "ed6bf75a-a3f6-4454-9391-6cec6d3b520b",
        "health": 98,
        "length": 3,
        "taunt": "D.Va online.",
        "name": "D.Va",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 10,
              "y": 3
            },
            {
              "object": "point",
              "x": 10,
              "y": 2
            },
            {
              "object": "point",
              "x": 9,
              "y": 2
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "c3e89743-fbdd-465b-8208-45ea0919b05a",
        "health": 98,
        "length": 3,
        "taunt": "UVIC FRESHIES",
        "name": "test",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 2,
              "y": 15
            },
            {
              "object": "point",
              "x": 2,
              "y": 14
            },
            {
              "object": "point",
              "x": 1,
              "y": 14
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "a9a2f79e-f6d0-4bd0-9531-b36cfa9de050",
        "health": 98,
        "length": 3,
        "taunt": "battlesnake-python!",
        "name": "squatchy-snake-2018",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 9,
              "y": 6
            },
            {
              "object": "point",
              "x": 9,
              "y": 7
            },
            {
              "object": "point",
              "x": 10,
              "y": 7
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "f56ed643-d88a-4638-914e-b9b3c8cf58b3",
        "health": 98,
        "length": 3,
        "taunt": "Do battle snakes dream of electric apples?",
        "name": "Batty Snake",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 0,
              "y": 7
            },
            {
              "object": "point",
              "x": 1,
              "y": 7
            },
            {
              "object": "point",
              "x": 2,
              "y": 7
            }
          ],
          "object": "list"
        }
      }
    ],
    "object": "list"
  },
  "food": {
    "data": [
      {
        "object": "point",
        "x": 4,
        "y": 8
      },
      {
        "object": "point",
        "x": 11,
        "y": 10
      },
      {
        "object": "point",
        "x": 12,
        "y": 17
      },
      {
        "object": "point",
        "x": 1,
        "y": 10
      },
      {
        "object": "point",
        "x": 8,
        "y": 5
      },
      {
        "object": "point",
        "x": 5,
        "y": 15
      },
      {
        "object": "point",
        "x": 6,
        "y": 3
      },
      {
        "object": "point",
        "x": 6,
        "y": 16
      },
      {
        "object": "point",
        "x": 8,
        "y": 11
      },
      {
        "object": "point",
        "x": 4,
        "y": 11
      },
      {
        "object": "point",
        "x": 1,
        "y": 0
      },
      {
        "object": "point",
        "x": 12,
        "y": 11
      },
      {
        "object": "point",
        "x": 12,
        "y": 10
      }
    ],
    "object": "list"
  },
  "object": "world",
  "dead_snakes": {
    "data": [
      {
        "id": "f53852c5-ad90-479b-874f-d2799d98c48a",
        "health": 98,
        "length": 3,
        "taunt": "right, down",
        "name": "hmm",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 7,
              "y": 2
            },
            {
              "object": "point",
              "x": 6,
              "y": 2
            },
            {
              "object": "point",
              "x": 7,
              "y": 2
            }
          ],
          "object": "list"
        }
      }
    ],
    "object": "list"
  },
  "you": {
    "id": "c3e89743-fbdd-465b-8208-45ea0919b05a",
    "health": 98,
    "length": 3,
    "taunt": "UVIC FRESHIES",
    "name": "test",
    "object": "snake",
    "body": {
      "data": [
        {
          "object": "point",
          "x": 2,
          "y": 15
        },
        {
          "object": "point",
          "x": 2,
          "y": 14
        },
        {
          "object": "point",
          "x": 1,
          "y": 14
        }
      ],
      "object": "list"
    }
  }
}


print 'checking init'
game = board(data['width'], data['height'], data['you'], data['snakes'])
print "game height should be 20:", game.height
print "game width should be 20:", game.width
print "the width of the game board should be 20:",len(game.board)
print "the height of the game board arr should be 20:", len(game.board[0])
print 'testing the plot case 1: top left corner'
game.plot(0,0,7)
if game.board[0][0] == 7:
    print 'pass plot'
else:
    print 'failed plot'
game.board[0][0] = 0
print 'testing the plot case 2: bottom right corner'
game.plot(game.width-1, game.height-1, 7)
if game.board[game.width-1][game.height-1] == 7:
    print 'pass plot'
else:
    print 'failed plot'
game.board[game.width-1][game.height-1] = 0
print 'testing snakes method:'
game.Snakes(game.other_snakes)
row = []
for y in range(0, game.height):
    for x in range(0, game.width):
        row.append(game.board[x][y])
    print row
    row = []

print 'testing self plot:'
game.plotSelf()
row = []
for y in range(0, game.height):
    for x in range(0, game.width):
        row.append(game.board[x][y])
    print row
    row = []
print 'check should return all directions:', game.check()