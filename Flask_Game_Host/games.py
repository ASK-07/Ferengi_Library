'''
Dictionary storing information about games offered on the site

Each key '<game>' is the same as its route string and stores:

    gameDict<game>[0]: Title of game
    gameDict<game>[1]: Name of game's image file
    gameDict<game>[2]: Short description of the game
    gameDict<game>[3]: URL of game's source repository

'''
gameDict = {

            'chess': ['Chess',
                            'Chess.jpg',
                            'Chess Classic',
                            'https://play.famobi.com/chess-classic'
                            ],

            'multi-square': ['Multi-Square',
                            'Multisquare.jpg',
                            'Multi-Square',
                            'https://play.famobi.com/multisquare'
                            ],

            'billiard': ['Billiard',
                            '8BallBilliards.jpg',
                            '8-Ball-Billiard',
                            'https://play.famobi.com/8-ball-billiards-classic'
                            ],

            'cannon-balls-3d': ['Cannon-Balls-3D',
                            'CannonBalls3d.jpg',
                            'Cannon-Balls-3D',
                            'https://play.famobi.com/cannon-balls-3d'
                            ],

            'archery-tour': ['Archery',
                            'ArcheryWorldTour.jpg',
                            'Archery World Tour',
                            'https://play.famobi.com/archery-world-tour'
                            ],

            'bowling': ['Bowling',
                            'ClassicBowling.jpg',
                            'Classic Bowling',
                            ' https://play.famobi.com/classic-bowling'
                            ],
            
            'table-tennis': ['Table-Tennis',
                            'TableTennis.jpg',
                            'Table Tennis World Tour',
                            'https://play.famobi.com/table-tennis-world-tour'
                            ],

            'checkers': ['Checkers',
                            'CheckersClassic.jpg',
                            'Checkers Classic',
                            'https://play.famobi.com/checkers-classic'
                            ]
            }