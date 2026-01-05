"""Effect for Darkshire Librarian (CORE_OG_109).

Card Text: <b>Battlecry:</b>
Discard a random card. <b>Deathrattle:</b>
Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)


def deathrattle(game, source):
    pass