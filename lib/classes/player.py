class Player:
    all = []

    def __init__(self, username):
        self._username = username
        Player.all.append(self)

    @property 
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if type(new_username) is str and 2 <= len(new_username) <= 16:
            self._username = new_username
        else:
            raise Exception("Username must be a string between 2 and 16 characters")

    def results(self):
        return [ result for result in Result.all if result.player is self]
        

    def games_played(self):
        return list (set ( [result.game for result in self.results()]))

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        all_games_i_have_played = [result.game for result in self.results()]
        return all_games_i_have_played.count(game)

    @classmethod
    def highest_scored(cls, game):
        pass

from classes.result import Result
from classes.game import Game