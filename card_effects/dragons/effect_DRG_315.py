"""Effect for Embiggen (DRG_315).

Card Text: Give all minions in your deck +2/+2. They cost (1) more <i>(up to 10)</i>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2