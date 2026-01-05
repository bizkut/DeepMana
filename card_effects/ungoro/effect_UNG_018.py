"""Effect for Flame Geyser (UNG_018).

Card Text: Deal $2 damage.
Add a 1/2 Elemental to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)