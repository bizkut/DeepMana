"""Effect for Shadow Word: Undeath (RLK_815).

Card Text: Deal $2 damage to all enemies. If a friendly Undead died after your last turn, deal $2 more.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)