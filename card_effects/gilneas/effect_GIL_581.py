"""Effect for Sandbinder (GIL_581).

Card Text: <b>Battlecry:</b> Draw an Elemental from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)