"""Effect for Eternal Sentinel (OG_026).

Card Text: <b>Battlecry:</b> Unlock your <b>Overloaded</b> Mana Crystals.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass