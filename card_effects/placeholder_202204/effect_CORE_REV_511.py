"""Effect for Bibliomite (CORE_REV_511).

Card Text: [x]<b>Battlecry</b>: Choose a card
 in your hand to shuffle
 into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass