"""Effect for Nascent Bolt (TIME_216).

Card Text: Deal $5 damage to a minion. If it survives, draw 2 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)