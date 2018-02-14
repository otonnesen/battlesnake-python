from board import board
data = {
  "width": 10,
  "height": 18,
  "id": 933,
  "turn": 114,
  "snakes": {
    "data": [
      {
        "id": "64f03f9f-c332-4330-8a1e-8342c8d887c7",
        "health": 81,
        "length": 5,
        "taunt": "Boop the snoot!",
        "name": "LUL",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 4,
              "y": 4
            },
            {
              "object": "point",
              "x": 4,
              "y": 5
            },
            {
              "object": "point",
              "x": 3,
              "y": 5
            },
            {
              "object": "point",
              "x": 3,
              "y": 4
            },
            {
              "object": "point",
              "x": 3,
              "y": 3
            }
          ],
          "object": "list"
        }
      },
      {
        "id": "c3e89743-fbdd-465b-8208-45ea0919b05a",
        "health": 92,
        "length": 7,
        "taunt": "<(O.o)>",
        "name": "test",
        "object": "snake",
        "body": {
          "data": [
            {
              "object": "point",
              "x": 4,
              "y": 2
            },
            {
              "object": "point",
              "x": 5,
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
            },
            {
              "object": "point",
              "x": 8,
              "y": 2
            },
            {
              "object": "point",
              "x": 8,
              "y": 3
            },
            {
              "object": "point",
              "x": 7,
              "y": 3
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
        "x": 9,
        "y": 3
      },
      {
        "object": "point",
        "x": 5,
        "y": 0
      },
      {
        "object": "point",
        "x": 8,
        "y": 1
      },
      {
        "object": "point",
        "x": 8,
        "y": 16
      },
      {
        "object": "point",
        "x": 2,
        "y": 12
      },
      {
        "object": "point",
        "x": 3,
        "y": 16
      },
      {
        "object": "point",
        "x": 8,
        "y": 11
      },
      {
        "object": "point",
        "x": 7,
        "y": 6
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
    "health": 92,
    "length": 7,
    "taunt": "<(O.o)>",
    "name": "test",
    "object": "snake",
    "body": {
      "data": [
        {
          "object": "point",
          "x": 4,
          "y": 2
        },
        {
          "object": "point",
          "x": 5,
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
        },
        {
          "object": "point",
          "x": 8,
          "y": 2
        },
        {
          "object": "point",
          "x": 8,
          "y": 3
        },
        {
          "object": "point",
          "x": 7,
          "y": 3
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
game.Snakes()
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

#Verifying ability to commit
#^ -Mack
#Test 2 as Mack, not root
