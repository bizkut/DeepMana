"""Effect for Bulk Up (BAR_841).

Card Text: Give a random <b>Taunt</b> minion in your hand +1/+1 and copy it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1