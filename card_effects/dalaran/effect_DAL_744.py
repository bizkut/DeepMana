"""Effect for Faceless Rager (DAL_744).

Card Text: <b>Battlecry:</b> Copy a friendly minion's Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)