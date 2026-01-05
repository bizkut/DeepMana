"""Effect for Timeless Blessing (WON_051).

Card Text: Give four random minions in your hand +4/+4, +3/+3, +2/+2, and +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4