"""Effect for Aimed Shot (SW_321).

Card Text: Deal $3 damage. Your next Hero Power deals 2 more damage.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)