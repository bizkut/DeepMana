"""Effect for Sinister Strike (CORE_CS2_075).

Card Text: Deal $3 damage to the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)