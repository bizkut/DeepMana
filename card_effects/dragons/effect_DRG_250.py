"""Effect for Fiendish Rites (DRG_250).

Card Text: <b>Invoke</b> Galakrond.
Give your minions +1 Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1