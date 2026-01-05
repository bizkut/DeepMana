"""Effect for Crazed Alchemist (EX1_059).

Card Text: <b>Battlecry:</b> Swap the Attack and Health of a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)