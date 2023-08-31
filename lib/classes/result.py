class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property 
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if type(new_score) is int and new_score in range(1,5001):
            self._score = new_score
        else:
            raise Exception("Score must be a number value between 1 and 5000")
    
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
        if type(new_player) is Player:
            self._player = new_player
        else:
            raise Exception("Player must be of Player Class")

    @property 
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if type(new_game) is Game:
            self._game = new_game
        else:
            raise Exception("Game must be of Game Class")


 
from classes.game import Game
from classes.player import Player