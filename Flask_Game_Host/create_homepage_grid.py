import games_dictionary

def fill_default_grid():
    '''
    Uses dictionary of games to create HTML string containing aggregate of game-cell divs

    Grid style can be modified in homepage.html

    '''
    # Get dictionary storing game info
    gamesDictionary = games_dictionary.gameDict

    # Initialize HTML string of game-cell divs to empty
    game_cells = ''

    # Build each cell of game grid using dictionary
    for game in gamesDictionary.keys():

        # Fetch info about current game
        game_title = gamesDictionary[game][0]
        game_image = gamesDictionary[game][1]
        game_description = gamesDictionary[game][2]

        # Create html string for current game's image
        image_string = '<img src="img/' + game_image + '" alt="' + game_image + '"/>'

        # Keeping this here to remember the pain
        # image_string = '<img src="{{ url_for(\'static\', filename=\'' + game_image + '\') }}" alt="' + game_image + '" class="image" />'

        # Initialize current game-cell div
        game_cells += '<div class="game-cell">'

        # Turn current game's info into complete game-cell div
        game_cells += image_string
        game_cells += '<br><u>'
        game_cells += game_title
        game_cells += '</u><br>'
        game_cells += game_description
        game_cells += '</div>'
    
    return game_cells
