"""Effect for Molten Blast (SCH_271).

Card Text: Deal $2 damage. Summon that many 1/1 Elementals.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)