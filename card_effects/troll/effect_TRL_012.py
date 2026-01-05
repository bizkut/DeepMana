"""Effect for Totemic Smash (TRL_012).

Card Text: Deal $2 damage. <b>Overkill</b>: Summon a basic Totem.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)