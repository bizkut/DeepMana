"""Effect for Barrens Trapper (BAR_082).

Card Text: Your <b>Deathrattle</b> cards
cost (1) less.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass