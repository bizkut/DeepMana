"""Effect for Devilsaur Mask (DINO_403).

Card Text: Set a minion's stats to 8/8. Give it <b>Charge</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 8
        target._max_health += 8