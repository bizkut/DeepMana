"""Effect for Dragon's Breath (BRM_003).

Card Text: Deal $4 damage. Costs (1) less for each minion that died this turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)