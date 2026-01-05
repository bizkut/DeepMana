"""Effect for Bogbeam (BT_134).

Card Text: Deal $3 damage to a minion.
Costs (0) if you have at least 7 Mana Crystals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)