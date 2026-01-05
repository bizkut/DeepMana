"""Effect for Naval Mine (TSC_001).

Card Text: [x]<b>Deathrattle:</b> Deal 4 damage
to the enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)