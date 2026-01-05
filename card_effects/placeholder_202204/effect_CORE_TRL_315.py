"""Effect for Pyromaniac (CORE_TRL_315).

Card Text: Whenever your Hero Power kills a minion, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)