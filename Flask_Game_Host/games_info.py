'''
Dictionary storing information about games offered on the site

Each key '<game>' stores:

    gameDict<game>[0]: Title of game
    gameDict<game>[1]: Name of game's image file
    gameDict<game>[2]: Short description of the game
    gameDict<game>[3]: URL of game's source repository

'''
gameDict = {'chess': ['Python Chess',
                      'chess.png',
                      'Classic tabletop chess',
                      'https://github.com/niklasf/python-chess/tree/master'
                      ],

            'pinball': ['Pinball',
                        'pinball.png',
                        'Classic pinball',
                        'URL'
                        ],

            'test_game_0': ['test_title_0',
                            'test_image_0.png',
                            'test_description_0',
                            'test_URL_0'
                            ],

            'test_game_1': ['test_title_1',
                            'test_image_1.png',
                            'test_description_1',
                            'test_URL_1'
                            ],

            'test_game_2': ['test_title_2',
                            'test_image_2.png',
                            'test_description_2',
                            'test_URL_2'
                            ]
            }

# def getGameDict():
#     return gameDict