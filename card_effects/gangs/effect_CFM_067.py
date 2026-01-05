"""Effect for Hozen Healer (CFM_067).

Card Text: <b>Battlecry</b>: Restore a minion to full Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)