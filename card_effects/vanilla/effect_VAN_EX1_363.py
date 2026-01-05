"""Effect for Blessing of Wisdom (VAN_EX1_363).

Card Text: Choose a minion. Whenever it attacks, draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)