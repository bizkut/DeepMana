"""Effect for Nozari (DAL_581).

Card Text: <b>Battlecry:</b> Restore both heroes to full Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)