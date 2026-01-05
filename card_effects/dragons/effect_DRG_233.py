"""Effect for Sand Breath (DRG_233).

Card Text: [x]Give a minion +1/+2.
Give it <b>Divine Shield</b> if
you're holding a Dragon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1