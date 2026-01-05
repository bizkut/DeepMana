"""Effect for Grand Magus Antonidas (SW_113).

Card Text: [x]<b>Battlecry:</b> If you've cast a
Fire spell on each of your last
three turns, cast 3 Fireballs at
   random enemies.@ <i>(@/3)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass