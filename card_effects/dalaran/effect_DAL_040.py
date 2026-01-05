"""Effect for Hench-Clan Shadequill (DAL_040).

Card Text: <b>Deathrattle:</b> Restore 5 Health to the enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)