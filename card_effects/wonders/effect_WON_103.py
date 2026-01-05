"""Effect for Chamber of Viscidus (WON_103).

Card Text: [x]Look at 3 cards in your
hand and choose one to
discard. Draw two cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)