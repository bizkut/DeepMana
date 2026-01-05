"""Effect for Bracing Cold (ONY_013).

Card Text: [x]Restore #5 Health to
your hero. Reduce the
Cost of a random spell
in your hand by (2).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)