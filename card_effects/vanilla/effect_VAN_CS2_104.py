"""Effect for Rampage (VAN_CS2_104).

Card Text: Give a damaged minion +3/+3.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3