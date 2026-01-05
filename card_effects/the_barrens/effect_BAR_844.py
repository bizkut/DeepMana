"""Effect for Outrider's Axe (BAR_844).

Card Text: After your hero attacks and kills a minion, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)