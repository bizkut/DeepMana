"""Effect for Glacial Advance (RLK_512).

Card Text: Deal $4 damage.
Your next spell this turn costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)