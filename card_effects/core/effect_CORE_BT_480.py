"""Effect for Crimson Sigil Runner (CORE_BT_480).

Card Text: <b>Outcast:</b> Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)