"""Effect for Holy Light (CORE_CS2_089).

Card Text: Restore #8 Health to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)