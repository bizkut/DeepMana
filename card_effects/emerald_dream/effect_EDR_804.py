"""Effect for Divination (EDR_804).

Card Text: Destroy a friendly Wisp to draw 3 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)