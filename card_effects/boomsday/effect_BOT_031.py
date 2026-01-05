"""Effect for Goblin Bomb (BOT_031).

Card Text: [x]<b>Deathrattle:</b> Deal 2 damage
to the enemy hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)