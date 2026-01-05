"""Effect for Curio Collector (GIL_640).

Card Text: Whenever you draw a card, gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)