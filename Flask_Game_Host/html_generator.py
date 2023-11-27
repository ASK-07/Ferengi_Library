from Flask_Game_Host.games import gameDict

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

        # Turn current game into game-cell div
        game_cells += '<div class="game-cell">'                                     # Open game-cell div
        game_cells += game_anchor + image_string + '</a><br>'                       # Add anchored image
        game_cells += game_anchor + '<u>' + game_title + '</u></a><br></div>'       # Add anchored title, close div
    
    return game_cells


def fill_grid_from_db(games_dict):

    # Initialize empty return string
    game_cells = ''

    # Build each cell of grid using dictionary parameter
    for game in games_dict.keys():

        # Fetch relevant info for grid
        flask_url = games_dict[game]['name']
        display_name = games_dict[game]['display_name']
        game_image = games_dict[game]['img_name']

        # Create string for opening anchor to game's page
        game_anchor = f'<a href="/OpenSourceGames/{flask_url}">'

        # Create string for loading current game's image
        image_string = f'<img src="img/{game_image}" alt="{game_image}"/>'

        # Turn current game into game-cell div
        game_cells += (
            '<div class="game-cell">'                               # Open game-cell
            f'{game_anchor}{image_string}</a><br>'                  # Anchor image
            f'{game_anchor}<u>{display_name}</u></a><br></div>'       # Anchor title, close game-cell
        )

    return game_cells
