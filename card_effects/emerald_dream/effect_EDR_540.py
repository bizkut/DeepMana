"""Effect for Twisted Webweaver (EDR_540).

Card Text: [x]Whenever you play another
minion you've already
played, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)