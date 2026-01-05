"""Effect for Cathedral of Atonement (REV_290).

Card Text: Give a minion +2/+1 and draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)