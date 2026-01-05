"""Effect for Seal of Light (GVG_057).

Card Text: Restore #4 Health to your hero and gain +2 Attack this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)