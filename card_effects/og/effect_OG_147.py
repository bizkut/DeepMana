"""Effect for Corrupted Healbot (OG_147).

Card Text: <b>Deathrattle:</b> Restore #8 Health to the enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)