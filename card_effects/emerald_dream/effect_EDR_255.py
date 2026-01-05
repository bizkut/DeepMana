"""Effect for Renewing Flames (EDR_255).

Card Text: <b>Lifesteal</b>. Deal $5 damage to the lowest Health enemy, twice.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)