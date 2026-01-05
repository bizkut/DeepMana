"""Effect for Blood Razor (ICC_064).

Card Text: <b>Battlecry and Deathrattle:</b>
Deal 1 damage to all minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)


def deathrattle(game, source):
    pass