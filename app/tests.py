from board import board
data = {
  "width": 17,
  "height": 14,
  "id": 54,
  "turn": 4,
  "snakes": {
    "data": [
      {
        "id": "fbfe1ab5-7616-4de4-8328-a7a9f57b4133",
        "health": 96,
        "length": 3,
        "taunt": "up",
        "name": "Leechy Snake",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 8,
              "y": 9
            },
            {
              "object": "point",
              "x": 8,
              "y": 10
            },
            {
              "object": "point",
              "x": 8,
              "y": 11
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "ed6bf75a-a3f6-4454-9391-6cec6d3b520b",
        "health": 100,
        "length": 4,
        "taunt": "Ready, player 1.",
        "name": "D.Va",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 3,
              "y": 2
            },
            {
              "object": "point",
              "x": 2,
              "y": 2
            },
            {
              "object": "point",
              "x": 2,
              "y": 3
            },
            {
              "object": "point",
              "x": 2,
              "y": 3
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "49bd6da9-1970-41b1-8d99-c32c484b943b",
        "health": 96,
        "length": 3,
        "taunt": "Awww! But I was going into Tosche Station to pick up some power converters!!!",
        "name": "snek v4",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 5,
              "y": 8
            },
            {
              "object": "point",
              "x": 5,
              "y": 7
            },
            {
              "object": "point",
              "x": 4,
              "y": 7
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "c3e89743-fbdd-465b-8208-45ea0919b05a",
        "health": 96,
        "length": 3,
        "taunt": "UVIC FRESHIES",
        "name": "test",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 7,
              "y": 10
            },
            {
              "object": "point",
              "x": 6,
              "y": 10
            },
            {
              "object": "point",
              "x": 5,
              "y": 10
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
        "x": 0,
        "y": 2
      },
      {
        "object": "point",
        "x": 3,
        "y": 7
      }
    ],
    "object": "list"
  },
  "object": "world",
  "dead_snakes": {
    "data": [],
    "object": "list"
  },
  "you": {
    "id": "c3e89743-fbdd-465b-8208-45ea0919b05a",
    "health": 96,
    "length": 3,
    "taunt": "UVIC FRESHIES",
    "name": "test",
    "object": "snake",
    "body": {
      "data": [
        {
          "object": "point",
          "x": 7,
          "y": 10
        },
        {
          "object": "point",
          "x": 6,
          "y": 10
        },
        {
          "object": "point",
          "x": 5,
          "y": 10
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

n = game.checkWalls()
print 'checking walls should return down', n
print 'checking snake part this returns moves', game.checkSnakes(n)
print 'check should return possible directions:', game.check()