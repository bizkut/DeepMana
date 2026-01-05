"""Effect for Upgraded Repair Bot (GVG_083).

Card Text: <b>Battlecry:</b> Give a friendly Mech +4 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)