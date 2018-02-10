from board import board
data = {
  "width": 19,
  "height": 15,
  "id": 2300,
  "turn": 60,
  "snakes": {
    "data": [
      {
        "id": "c3e89743-fbdd-465b-8208-45ea0919b05a",
        "health": 91,
        "length": 5,
        "taunt": "UVIC FRESHIES",
        "name": "test",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 17,
              "y": 1
            },
            {
              "object": "point",
              "x": 17,
              "y": 0
            },
            {
              "object": "point",
              "x": 18,
              "y": 0
            },
            {
              "object": "point",
              "x": 18,
              "y": 1
            },
            {
              "object": "point",
              "x": 18,
              "y": 2
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "f56ed643-d88a-4638-914e-b9b3c8cf58b3",
        "health": 99,
        "length": 8,
        "taunt": "Do battle snakes dream of electric apples?",
        "name": "Batty Snake",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 2,
              "y": 12
            },
            {
              "object": "point",
              "x": 1,
              "y": 12
            },
            {
              "object": "point",
              "x": 1,
              "y": 13
            },
            {
              "object": "point",
              "x": 2,
              "y": 13
            },
            {
              "object": "point",
              "x": 3,
              "y": 13
            },
            {
              "object": "point",
              "x": 4,
              "y": 13
            },
            {
              "object": "point",
              "x": 5,
              "y": 13
            },
            {
              "object": "point",
              "x": 6,
              "y": 13
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
        "x": 17,
        "y": 10
      },
      {
        "object": "point",
        "x": 8,
        "y": 14
      },
      {
        "object": "point",
        "x": 15,
        "y": 10
      },
      {
        "object": "point",
        "x": 18,
        "y": 11
      },
      {
        "object": "point",
        "x": 2,
        "y": 14
      }
    ],
    "object": "list"
  },
  "object": "world",
  "dead_snakes": {
    "data": [
      {
        "id": "17f2b256-6e93-4cc9-abfe-ce957a227bb0",
        "health": 97,
        "length": 3,
        "taunt": "battlesnake-python!",
        "name": "2017 bounty-swu-ake",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": -1,
              "y": 4
            },
            {
              "object": "point",
              "x": 0,
              "y": 4
            },
            {
              "object": "point",
              "x": 1,
              "y": 4
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "a9a2f79e-f6d0-4bd0-9531-b36cfa9de050",
        "health": 97,
        "length": 4,
        "taunt": "battlesnake-python!",
        "name": "squatchy-snake-2018",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 3,
              "y": 1
            },
            {
              "object": "point",
              "x": 2,
              "y": 1
            },
            {
              "object": "point",
              "x": 3,
              "y": 1
            },
            {
              "object": "point",
              "x": 3,
              "y": 0
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "64f03f9f-c332-4330-8a1e-8342c8d887c7",
        "health": 56,
        "length": 3,
        "taunt": "Boop the snoot!",
        "name": "LUL",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 8,
              "y": 6
            },
            {
              "object": "point",
              "x": 8,
              "y": 7
            },
            {
              "object": "point",
              "x": 9,
              "y": 7
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
    "health": 91,
    "length": 5,
    "taunt": "UVIC FRESHIES",
    "name": "test",
    "object": "snake",
    "body": {
      "data": [
        {
          "object": "point",
          "x": 17,
          "y": 1
        },
        {
          "object": "point",
          "x": 17,
          "y": 0
        },
        {
          "object": "point",
          "x": 18,
          "y": 0
        },
        {
          "object": "point",
          "x": 18,
          "y": 1
        },
        {
          "object": "point",
          "x": 18,
          "y": 2
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

print 'checking walls should return down', game.checkWalls()
print 'checking snake part', game.checkSnakes()
print 'check should return all directions:', game.check()