"""Effect for Overwhelm (SCH_604).

Card Text: Deal $2 damage to a minion. Deal one more damage for each Beast you control.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)