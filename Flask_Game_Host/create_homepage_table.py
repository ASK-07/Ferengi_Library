import games_info

def build_default_table():
    '''
    Create a table using HTML to display all games offered on the site

    A maximum of 4 games are displayed per row

    '''
    # Get dictionary storing game info
    gamesInfo = games_info.gameDict

    # Initialize HTML string that creates a table of games and opens first row
    html_string = '<table class =\"Games\"><tr>'

    # Loop through each game in dictionary and add it to the table
    col_count = 0
    for game in gamesInfo.keys():

        game_title = gamesInfo[game][0]       # Fetch title of current game

        # Cap number of games per row to 4
        if col_count < 4:
            html_string += '<td>'             # Open new column

            # Add game_title to new column
            html_string += game_title

            html_string += '</td>'            # Close current column
            col_count += 1
        else:
            html_string += '</tr><tr><td>'    # Close previous row, open new row, open new column
            col_count = 0

            # Add game_title to new column in new row
            html_string += game_title

            html_string += '</td>'            # Close current column
            col_count += 1

    # Close table
    html_string += '</table>'

    return html_string
