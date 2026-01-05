"""Effect for Piercing Shot (BAR_032).

Card Text: Deal $6 damage to a minion. Excess damage hits the enemy hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 6, source)