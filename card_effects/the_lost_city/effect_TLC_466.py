"""Effect for Story of Lakkari (TLC_466).

Card Text: [x]At the end of your turn,
discard a card and fill
your board with 3/2 Imps.
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass