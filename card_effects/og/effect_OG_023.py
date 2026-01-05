"""Effect for Primal Fusion (OG_023).

Card Text: Give a minion +1/+1 for each of your Totems.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1