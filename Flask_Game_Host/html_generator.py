from games import gameDict

def fill_grid():
    '''
    Uses dictionary of games to create HTML string containing aggregate of game-cell divs

    '''
    # Get dictionary storing game info
    gamesDictionary = gameDict

    # Initialize HTML string of game-cell divs to empty
    game_cells = ''

    # Build each cell of grid using dictionary
    for game in gamesDictionary.keys():

        # Fetch info about current game
        game_title = gamesDictionary[game][0]
        game_image = gamesDictionary[game][1]
        game_description = gamesDictionary[game][2]

        # Create open anchor for game's page
        game_anchor = '<a href="/' + game + '">'

        # Create html string that loads current game's image
        image_string = '<img src="img/' + game_image + '" alt="' + game_image + '"/>'

        # Keeping this here to remember the pain
        # image_string = '<img src="{{ url_for(\'static\', filename=\'' + game_image + '\') }}" alt="' + game_image + '" class="image" />'

        # Turn current game into game-cell div
        game_cells += '<div class="game-cell">'                             # Open game-cell div
        game_cells += game_anchor + image_string + '</a><br>'               # Add anchored image
        game_cells += game_anchor + '<u>' + game_title + '</u></a><br>'     # Add anchored title
        game_cells += game_description + '</div>'                           # Add description, close div
    
    return game_cells
