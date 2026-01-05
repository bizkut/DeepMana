"""Effect for Lava Burst (EX1_241).

Card Text: Deal $5 damage. <b>Overload:</b> (2)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 5, source)