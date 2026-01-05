"""Effect for Leper Gnome (EX1_029).

Card Text: <b>Deathrattle:</b> Deal 2 damage to the enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)