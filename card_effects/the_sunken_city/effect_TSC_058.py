"""Effect for Predation (TSC_058).

Card Text: Deal $2 damage.
Costs (0) if you played a Naga while holding this.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)