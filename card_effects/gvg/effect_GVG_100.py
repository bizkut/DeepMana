"""Effect for Floating Watcher (GVG_100).

Card Text: Whenever your hero takes damage on your turn, gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2