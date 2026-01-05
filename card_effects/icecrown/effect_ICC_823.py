"""Effect for Simulacrum (ICC_823).

Card Text: Copy the lowest Cost minion in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass