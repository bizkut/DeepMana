"""Effect for Darkspear Berserker (BAR_027).

Card Text: <b>Deathrattle:</b> Deal 5 damage to your hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)