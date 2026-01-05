"""Effect for Leatherworking Kit (SW_457).

Card Text: [x]After three friendly
Beasts die, draw a Beast
and give it +1/+1.
Lose 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)