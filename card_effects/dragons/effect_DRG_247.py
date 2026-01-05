"""Effect for Seal Fate (DRG_247).

Card Text: Deal $3 damage to an undamaged character. <b>Invoke</b> Galakrond.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 3, source)