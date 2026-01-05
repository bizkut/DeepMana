"""Effect for Mana Burn (BT_753).

Card Text: Your opponent has 2 fewer Mana Crystals next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass