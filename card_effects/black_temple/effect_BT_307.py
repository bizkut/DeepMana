"""Effect for Darkglare (BT_307).

Card Text: <b>Battlecry:</b> If your hero took damage this turn, refresh 3 Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass