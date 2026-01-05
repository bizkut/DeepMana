"""Effect for Kobold Sandtrooper (ULD_184).

Card Text: <b>Deathrattle:</b> Deal 3 damage to the enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)