"""Effect for Backfire (YOP_033).

Card Text: Draw 3 cards. Deal $3 damage to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)