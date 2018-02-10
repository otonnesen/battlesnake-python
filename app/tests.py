from board import board
data = {
  "width": 13,
  "height": 22,
  "id": 2268,
  "turn": 7,
  "snakes": {
    "data": [
      {
        "id": "a4f76249-e34b-4e08-b55e-5b4f92731dfa",
        "health": 100,
        "length": 4,
        "taunt": "up",
        "name": "CrazyLeechy",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 0,
              "y": 14
            },
            {
              "object": "point",
              "x": 0,
              "y": 15
            },
            {
              "object": "point",
              "x": 0,
              "y": 16
            },
            {
              "object": "point",
              "x": 0,
              "y": 16
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "49bd6da9-1970-41b1-8d99-c32c484b943b",
        "health": 93,
        "length": 3,
        "taunt": "",
        "name": "snek v4",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 9,
              "y": 11
            },
            {
              "object": "point",
              "x": 8,
              "y": 11
            },
            {
              "object": "point",
              "x": 8,
              "y": 12
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "d159f700-e06a-4195-a1f9-8dccdfe56e7f",
        "health": 93,
        "length": 3,
        "taunt": "Outta my way, snake!",
        "name": "FooSnake",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 5,
              "y": 3
            },
            {
              "object": "point",
              "x": 5,
              "y": 4
            },
            {
              "object": "point",
              "x": 5,
              "y": 5
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "c3e89743-fbdd-465b-8208-45ea0919b05a",
        "health": 93,
        "length": 3,
        "taunt": "UVIC FRESHIES",
        "name": "test",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 11,
              "y": 21
            },
            {
              "object": "point",
              "x": 11,
              "y": 20
            },
            {
              "object": "point",
              "x": 11,
              "y": 19
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
        "x": 12,
        "y": 13
      },
      {
        "object": "point",
        "x": 9,
        "y": 9
      }
    ],
    "object": "list"
  },
  "object": "world",
  "dead_snakes": {
    "data": [
      {
        "id": "47ba8e18-3a1b-4894-9e50-bc910dc7b3f0",
        "health": 94,
        "length": 3,
        "taunt": "Outta my way, snake!",
        "name": "FooSnake",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 0,
              "y": -1
            },
            {
              "object": "point",
              "x": 0,
              "y": 0
            },
            {
              "object": "point",
              "x": 0,
              "y": 1
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "17f2b256-6e93-4cc9-abfe-ce957a227bb0",
        "health": 93,
        "length": 3,
        "taunt": "battlesnake-python!",
        "name": "2017 bounty-swu-ake",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 0,
              "y": 16
            },
            {
              "object": "point",
              "x": 1,
              "y": 16
            },
            {
              "object": "point",
              "x": 2,
              "y": 16
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
    "health": 93,
    "length": 3,
    "taunt": "UVIC FRESHIES",
    "name": "test",
    "object": "snake",
    "body": {
      "data": [
        {
          "object": "point",
          "x": 11,
          "y": 21
        },
        {
          "object": "point",
          "x": 11,
          "y": 20
        },
        {
          "object": "point",
          "x": 11,
          "y": 19
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
print 'check should return all directions:', game.check()