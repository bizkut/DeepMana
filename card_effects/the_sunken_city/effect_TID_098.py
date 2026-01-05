"""Effect for Myrmidon (TID_098).

Card Text: After you cast a spell on this minion, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)