"""Effect for Headcrack (VAN_EX1_137).

Card Text: Deal $2 damage to the enemy hero. <b>Combo:</b> Return this to your hand next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)