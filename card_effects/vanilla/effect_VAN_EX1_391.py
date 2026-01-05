"""Effect for Slam (VAN_EX1_391).

Card Text: Deal $2 damage to a minion. If it survives, draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)