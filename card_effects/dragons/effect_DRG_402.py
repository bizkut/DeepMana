"""Effect for Sathrovarr (DRG_402).

Card Text: <b>Battlecry:</b> Choose a friendly minion. Add a copy of it to your hand, deck, and battlefield.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass