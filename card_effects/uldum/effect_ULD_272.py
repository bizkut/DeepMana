"""Effect for Holy Ripple (ULD_272).

Card Text: Deal $1 damage to all enemies. Restore #1 Health to all friendly characters.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)