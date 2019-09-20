from play import *

p1 = Player()
p2 = Player('Jon', 'Stewart', 200)
p3 = Player('Stephen', 'Colbert', 300)

game1 = Game()

p1.place_bet(game1, [1,2,3], 50.0)
