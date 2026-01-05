"""Effect for Brittleskin Zombie (RLK_113).

Card Text: <b>Deathrattle:</b> If it's your opponent's turn, deal 3 damage to them.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)