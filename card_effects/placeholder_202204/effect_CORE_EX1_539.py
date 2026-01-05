"""Effect for Kill Command (CORE_EX1_539).

Card Text: Deal $3 damage. If you control a Beast, deal
$5 damage instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)