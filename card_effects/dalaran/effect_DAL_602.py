"""Effect for Plot Twist (DAL_602).

Card Text: Shuffle your hand
into your deck.
Draw that many cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)