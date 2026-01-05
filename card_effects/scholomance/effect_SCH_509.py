"""Effect for Brain Freeze (SCH_509).

Card Text: <b>Freeze</b> a minion. <b>Combo:</b> Also deal $3 damage to it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)