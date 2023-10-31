class Player :
  def __init__(self, username, score):
    self.username = username
    self.score = score
    

  def sort_players(player_list):
     return sorted(player_list, key=lambda obj: obj.score, reverse=True)
  