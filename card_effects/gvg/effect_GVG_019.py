"""Effect for Demonheart (GVG_019).

Card Text: Deal $5 damage to a minion.  If it's a friendly Demon, give it +5/+5 instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)