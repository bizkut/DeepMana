"""Effect for Smuggler's Run (CFM_305).

Card Text: Give all minions in your hand +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1