"""Effect for Bolster (AT_068).

Card Text: Give your <b>Taunt</b> minions +2/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2