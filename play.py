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


    def place_bet(self, game, bet_nums, amount):
        """Places a bet on one or several numbers dictated by 'numbers';
        numbers may take an int, list or string input."""

        print(self.fname,'is placing a bet: ',amount,'on',bet_nums)

        if amount > self.bank:
            print('Error <Player.place_bet>: Not enough money in bank')
        else:
            bet = Bet(bet_nums, amount)
            self.bank -= bet.amount
            game.add_bet(self, bet)


class Game:
    new_id = itertools.count(1)

    def __init__(self):
        self.all_bets = []
        self.id = next(Game.new_id)


    def add_bet(self, player, bet):
        """ Update list of bets in game."""
        self.all_bets.append((player, bet))


    def gen_winning_number():
        """ Spin the wheel and generate the winning number. 
        Assumes European wheel (no 00 value)."""
        return random.randint(0, 36)


    def communicate_win(self, player):
        """ Print win message to console"""
        print('Congratulations to',player.fname,player.lname,': you win!')


    def resolve(self):
        """ Finish game by choosing a number and paying out winners"""
        print('Spin the wheel!')
        w = Game.gen_winning_number()
        print('Winning number is... ',w,'!')
        for bets in self.all_bets:
            p, b = bets
            if w in b.bet_nums:
                self.communicate_win(p)
                Bet.payout(p, Bet.winnings(b.amount))


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


    def winnings(amount):
        return 36 * amount


    def payout(player, winnings):
        player.bank += winnings
