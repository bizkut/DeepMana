"""Effect for Mortal Coil (EX1_302).

Card Text: Deal $1 damage to a minion. If that kills it, draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)