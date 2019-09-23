# SB&G API Tech Test

This package simulates the fundamentals of a roulette game. You can create players and individual roulette games, and place bets, with the methods defined in the three classes `Player`, `Game`, `Bet`.


## Methods 

`Player`: initiate a player with a unique ID. The function `place_bet` calls a bet in a given game, for some set of numbers and some monetary amount. See also `Bet` below. Coding against a user interface, the appropriate method call can be mapped easily to a location on the roulette table.

`Game`: instantiate a single game (one spin of the wheel). All bets within this game are stored in the `all_bets` attribute. The central function is `resolve`, which concludes the game by generating the winning number and matching it to all bets placed. Winners are notified through the `communicate_win` method.

`Bet`: each instance is a single bet by a single player. The method `parse_inputs` accepts an integer or a list of integers. Methods `winnings` and `payout` calculate the amount won on a successful bet, and update the winner's account accordingly.  


## Alternatives and future development

An alternative implementation of the storage of bets in a game (`Game.all_bets`) may store bets in an external database, with puts and gets for the required data. 

The method `Bet.parse_input` may be extended to include 'named' bets in the method call, such as 'red', 'black', 'first dozen', 'voisins', etc. Each of these corresponds to a list of numbers, and is relatively straightforward to implement.

The `winnings` method calculates the amount won, by simply multiplying the amount per number called by 36. Case-specific deviations from this simple formula due to, say,  special game rules may be incorporated by modifying this method.


## To run

Requires Python 3.x with itertools and random. 

A test script simulating a single game is included in test.py. A game can also be played interactively in a terminal.

