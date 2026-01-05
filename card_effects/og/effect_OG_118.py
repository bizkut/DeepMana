"""Effect for Renounce Darkness (OG_118).

Card Text: Replace your Hero Power and Warlock cards with another class's. The cards cost (1) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass