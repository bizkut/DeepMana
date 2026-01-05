"""Effect for Crushing Hand (LOOT_060).

Card Text: Deal $8 damage to a minion. <b><b>Overload</b>:</b> (3)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 8, source)