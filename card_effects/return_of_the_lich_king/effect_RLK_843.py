"""Effect for Arcane Bolt (RLK_843).

Card Text: Deal $2 damage. <b>Manathirst (8):</b> Deal $3 damage instead.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)