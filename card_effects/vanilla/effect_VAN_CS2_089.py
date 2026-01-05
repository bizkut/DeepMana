"""Effect for Holy Light (VAN_CS2_089).

Card Text: Restore #6 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 6, source)