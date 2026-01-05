"""Effect for Hidden Wisdom (GIL_903).

Card Text: [x]<b>Secret:</b> After your
opponent plays three
cards in a turn, draw
2 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)