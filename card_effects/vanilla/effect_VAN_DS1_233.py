"""Effect for Mind Blast (VAN_DS1_233).

Card Text: Deal $5 damage to the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)