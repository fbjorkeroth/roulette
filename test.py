from play import *

p1 = Player()
p2 = Player('Jon', 'Stewart', 200)
p3 = Player('Stephen', 'Colbert', 300)

game1 = Game()

p1.place_bet(game1, [1,2,3], 50.0)
p2.place_bet(game1, 14, 10.0)
p3.place_bet(game1, 1, 10.0)
p2.place_bet(game1, 3, 200.0)
p1.place_bet(game1, [1,2,3,4.1], 1.0)
p2.place_bet(game1, [10,11,15,16], 10.0)
p1.place_bet(game1, [5,6,7,8], 7.50)

game1.resolve()
