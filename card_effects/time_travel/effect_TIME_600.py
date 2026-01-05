"""Effect for Precise Shot (TIME_600).

Card Text: Deal $3 damage.
If this is EXACTLY in the center of your hand,
deal $5 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)