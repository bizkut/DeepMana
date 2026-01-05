"""Effect for Lava Flow (TLC_227).

Card Text: Deal $2 damage to the lowest Health enemy, three times. <b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 2, source)