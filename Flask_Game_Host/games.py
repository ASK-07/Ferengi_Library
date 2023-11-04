'''
Dictionary storing information about games offered on the site

Each key '<game>' is the same as its route string and stores:

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
                        'https://github.com/corehtml5canvas/code/tree/master/ch09/pinball'
                        ],

            'test_game_0': ['test_title_0',
                            'gex.png',
                            'test_description_0',
                            'test_URL_0'
                            ],

            'test_game_1': ['test_title_1',
                            'smackdown.png',
                            'test_description_1',
                            'test_URL_1'
                            ],

            'test_game_2': ['test_title_2',
                            'homescapes.png',
                            'test_description_2',
                            'test_URL_2'
                            ],

            'test_game_3': ['test_title_3',
                            'bugsnax.png',
                            'test_description_3',
                            'test_URL_3'
                            ],

            'test_game_4': ['test_title_4',
                            'crying.png',
                            'test_description_4',
                            'test_URL_4'
                            ],

            'test_game_5': ['test_title_5',
                            'evil.png',
                            'test_description_5',
                            'test_URL_5'
                            ],
            
            'test_game_6': ['test_title_6',
                            'test_image_6.png',
                            'test_description_6',
                            'test_URL_6'
                            ],

            'test_game_7': ['test_title_7',
                            'test_image_7.png',
                            'test_description_7',
                            'test_URL_7'
                            ]
            }