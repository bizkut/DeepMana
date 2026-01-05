"""Effect for Shadowfiend (AT_014).

Card Text: Whenever you draw a card, reduce its Cost by (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)