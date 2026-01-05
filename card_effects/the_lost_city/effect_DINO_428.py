"""Effect for Behemoth Mask (DINO_428).

Card Text: [x]Set a minion's stats to
8/10 and give it <b>Lifesteal</b>.
Force a random enemy
minion to attack it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 8
        target._max_health += 8