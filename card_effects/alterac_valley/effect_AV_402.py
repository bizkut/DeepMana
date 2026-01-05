"""Effect for The Lobotomizer (AV_402).

Card Text: [x]<b>Honorable Kill:</b> Get a
copy of the top card
of your opponent's
deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass