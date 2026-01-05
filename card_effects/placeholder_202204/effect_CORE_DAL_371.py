"""Effect for Marked Shot (CORE_DAL_371).

Card Text: Deal $4 damage to a minion. <b>Discover</b> a spell.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)