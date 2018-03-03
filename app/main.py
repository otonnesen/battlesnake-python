# -*- coding: utf-8 -*-
import bottle
import os
import random
from board import board
<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')

"""
This start request only happens once so if we take in all the json data
into a object we can then just work with that object to speed things up
"""
@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']


    head_url = '%s://%s/static/head.gif' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#add8e6', #light blue
        'secondary_color': '#ffff00', # yellow
        'taunt': 'WOW',
        'head_url': "https://i.imgur.com/KdK8Eu9.gif",
        'name': 'Computer_Science_First_Years',
        'head_type': 'fang',
        'tail_type': 'pixel'
    }


@bottle.post('/move')
def move():  
    data = bottle.request.json
    """
    json format for snake
    interface Snake {
        body: List<Point>;
        health: number;
        id: string;
        length: number;
        name: string;
        object: 'snake';
        taunt: string;
    }
    """
    game_board = board(data['width'], data['height'], data['you'], data['snakes'], data['food'])
    game_board.run()
    moves = game_board.check()

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
    animations = ['( ͡° ͜ʖ ͡°)','ヽ༼ຈل͜ຈ༽ﾉ ʀᴀɪsᴇ ᴜʀ ᴅᴏɴɢᴇʀs ヽ༼ຈل͜ຈ༽ﾉ','( ͡ʘ╭͜ʖ╮͡ʘ)','( ͡⚆ ͜ʖ ͡⚆)','( ͡◉ ͜ʖ ͡◉)','(╯ຈل͜ຈ) ╯︵ ┻━┻']

    return {
        'move': random.choice(moves),
        'taunt': random.choice(animations)
    }



# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
    
