"""Effect for Acolyte of Pain (WON_357).

Card Text: Whenever this minion takes damage, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)