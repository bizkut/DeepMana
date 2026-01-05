"""Effect for Nozdormu the Timeless (DRG_309).

Card Text: <b>Battlecry:</b> Set each player to 10 Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass