"""Effect for Focused Will (CS3_027).

Card Text: <b>Silence</b> a minion, then give it +3 Health.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)