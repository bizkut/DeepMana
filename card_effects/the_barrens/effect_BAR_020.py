"""Effect for Razormane Raider (BAR_020).

Card Text: <b>Frenzy:</b> Attack a
random enemy.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass