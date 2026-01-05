"""Effect for Rain of Fire (DRG_206).

Card Text: Deal $1 damage to all characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)