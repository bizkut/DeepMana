"""Effect for Bonfire Elemental (GIL_645).

Card Text: <b>Battlecry:</b> If you played an Elemental last turn, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)