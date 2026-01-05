"""Effect for Nitroboost Poison (YOP_015).

Card Text: Give a minion +2 Attack.
<b>Corrupt:</b> And your weapon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2