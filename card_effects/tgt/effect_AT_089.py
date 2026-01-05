"""Effect for Boneguard Lieutenant (AT_089).

Card Text: <b>Inspire:</b> Gain +1 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)