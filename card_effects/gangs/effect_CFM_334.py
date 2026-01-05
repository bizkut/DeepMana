"""Effect for Smuggler's Crate (CFM_334).

Card Text: Give a random Beast in your hand +2/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2