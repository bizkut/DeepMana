"""Effect for Dragged Below (TSC_956).

Card Text: [x]Deal $4 damage
to a minion.
Give your opponent
an Abyssal Curse.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 4, source)