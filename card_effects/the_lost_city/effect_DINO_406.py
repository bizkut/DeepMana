"""Effect for Fire Breath (DINO_406).

Card Text: Deal $4 damage.
Give your Elementals +1/+1.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)