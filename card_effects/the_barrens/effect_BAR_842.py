"""Effect for Conditioning (Rank 1) (BAR_842).

Card Text: Give minions in your hand +1/+1. <i>(Upgrades when you have 5 Mana.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1