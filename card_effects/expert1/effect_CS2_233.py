"""Effect for Blade Flurry (CS2_233).

Card Text: Destroy your weapon and deal its damage to all enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    for m in list(opponent.board): game.deal_damage(m, 1, source)