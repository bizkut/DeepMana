"""Effect for Clash of the Colossals (TID_715).

Card Text: Add a random <b>Colossal</b> minion to both players' hands. Yours costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass