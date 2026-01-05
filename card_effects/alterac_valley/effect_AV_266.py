"""Effect for Windchill (AV_266).

Card Text: <b>Freeze</b> a minion.
Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)