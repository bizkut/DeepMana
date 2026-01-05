"""Effect for Shadowed Spirit (LEG_CS3_013).

Card Text: [x]<b>Deathrattle:</b> Deal 3
damage to the
enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)