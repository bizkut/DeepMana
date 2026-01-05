"""Effect for Freezing Potion (CFM_021).

Card Text: <b>Freeze</b> an enemy.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True