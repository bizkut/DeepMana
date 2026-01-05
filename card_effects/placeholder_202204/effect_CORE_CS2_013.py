"""Effect for Wild Growth (CORE_CS2_013).

Card Text: Gain an empty Mana Crystal.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass