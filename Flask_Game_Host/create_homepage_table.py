import games_info

def build_default_table():
    '''
    Create a table using HTML to display all games offered on the site

    Number of games to display per row can be changed by modifying max_cols

    '''
    # Get dictionary storing game info
    gamesInfo = games_info.gameDict

    # Initialize HTML string that creates a table of games and opens first row
    html_string = '<table class =\"Games\"><tr>'

    # Loop through each game in dictionary and add it to the table
    col_count = 0
    max_cols = 4                              # Number of games to display per row
    for game in gamesInfo.keys():

        # Fetch info about current game
        game_title = gamesInfo[game][0]
        game_description = gamesInfo[game][2]

        # Fill space in new column of current row with current game
        if col_count < max_cols:
            html_string += '<td>'             # Open new column

            html_string += game_title
            html_string += '<br>'
            html_string += game_description

            html_string += '</td>'            # Close current column
            col_count += 1
        
        # Fill space in first column of new row with current game
        else:
            col_count = 0
            html_string += '</tr><tr><td>'    # Close previous row, open new row, open new column

            # Fill table space
            html_string += game_title
            html_string += '<br>'
            html_string += game_description

            html_string += '</td>'            # Close current column
            col_count += 1

    html_string += '</table>'                 # Close table

    return html_string
