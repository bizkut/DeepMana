"""Effect for Blade Flurry (VAN_CS2_233).

Card Text: Destroy your weapon and deal its damage to all enemies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)