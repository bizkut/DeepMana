"""Effect for Mind Sear (NX2_019).

Card Text: Deal $2 damage to a minion. If it dies,
deal $3 damage to the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)