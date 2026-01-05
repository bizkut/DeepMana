"""Effect for Divine Favor (EX1_349).

Card Text: Draw cards until you have as many in hand as your opponent.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)