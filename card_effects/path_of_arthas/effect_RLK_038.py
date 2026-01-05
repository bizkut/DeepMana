"""Effect for Icy Touch (RLK_038).

Card Text: Deal $2 damage to an enemy and <b>Freeze</b> it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)