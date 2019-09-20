import itertools
import random


class Player:
    new_id = itertools.count(1)

    def __init__(self, fname='Jane', lname='Smith', bank=100):
        self.id = next(Player.new_id)
        self.fname = str(fname)
        self.lname = str(lname)
        try:
            self.bank = float(bank)
        except:
            print('Error <Player.__init__>: initial bank amount not a number.')
            self.bank = float(input('Input numerical value:'))


class Game:
    new_id = itertools.count(1)

    def __init__(self):
        self.id = next(Game.new_id)


class Bet:
    new_id = itertools.count(1)

    def __init__(self, bet_nums, amount):
        self.id = next(Bet.new_id)
        self.bet_nums = Bet.parse_input(bet_nums)
        self.amount = amount

    def parse_input(bet_nums):
        if isinstance(bet_nums, int):
            return [bet_nums]
        elif isinstance(bet_nums, (list, tuple)):
            return list(bet_nums)
        else:
            print('Error <Bet.parse_input>: bet not of recognised type')
            return None
