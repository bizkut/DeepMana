"""Effect for Veranus (DRG_095).

Card Text: <b>Battlecry:</b> Change the Health of all enemy minions to 1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)