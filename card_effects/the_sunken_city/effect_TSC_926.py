"""Effect for Smothering Starfish (TSC_926).

Card Text: <b>Battlecry:</b> <b>Silence</b> ALL other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)