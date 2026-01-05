"""Effect for Amber Watcher (DRG_226).

Card Text: <b>Battlecry:</b> Restore #8 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)