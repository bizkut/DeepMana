"""Effect for Need for Greed (DED_506).

Card Text: <b>Tradeable</b>
Draw 3 cards. If drawn this turn, this costs (3).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)