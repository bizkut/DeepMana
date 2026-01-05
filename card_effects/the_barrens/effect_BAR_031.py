"""Effect for Sunscale Raptor (BAR_031).

Card Text: <b>Frenzy:</b> Shuffle a Sunscale Raptor into your deck with permanent +2/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2