"""Effect for Barbed Nets (TSC_023).

Card Text: [x]Deal $2 damage to an
enemy. If you played a
Naga while holding this,
choose a second target.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)