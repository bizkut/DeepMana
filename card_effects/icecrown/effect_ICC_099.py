"""Effect for Ticking Abomination (ICC_099).

Card Text: <b>Deathrattle:</b> Deal 5 damage to your minions.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)