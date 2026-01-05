"""Effect for Dragon Breeder (DRG_070).

Card Text: <b>Battlecry:</b> Choose a friendly Dragon. Add a copy of it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass