"""Effect for Barbaric Sorceress (TSC_020).

Card Text: <b>Taunt</b>. <b>Battlecry:</b> Swap the Cost of a random spell in each player's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass