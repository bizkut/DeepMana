"""Effect for Drain Life (CS2_061).

Card Text: Deal $2 damage. Restore #2 Health to your hero.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)