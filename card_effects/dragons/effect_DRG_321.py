"""Effect for Rolling Fireball (DRG_321).

Card Text: Deal $8 damage to a minion. Any excess damage continues to
the left or right.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)