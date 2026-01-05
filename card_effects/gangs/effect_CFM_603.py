"""Effect for Potion of Madness (CFM_603).

Card Text: Gain control of an enemy minion with 2 or less Attack until end of turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass