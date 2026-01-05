"""Effect for Runed Mithril Rod (SW_003).

Card Text: [x]After you draw 4 cards,
reduce the Cost of cards
in your hand by (1).
Lose 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)