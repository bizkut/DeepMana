"""Effect for Fight Promoter (CFM_328).

Card Text: [x]<b>Battlecry:</b> If you control
a minion with 6 or more
 Health, draw two cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(6)