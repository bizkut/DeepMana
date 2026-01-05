"""Effect for Vengeful Spirit (BAR_328).

Card Text: <b>Outcast:</b> Draw 2 <b>Deathrattle</b> minions.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(2)