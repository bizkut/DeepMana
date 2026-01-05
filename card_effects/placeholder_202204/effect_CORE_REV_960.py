"""Effect for Ashen Elemental (CORE_REV_960).

Card Text: [x]<b>Battlecry:</b> Whenever your
opponent draws a card next
turn, they take 2 damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)