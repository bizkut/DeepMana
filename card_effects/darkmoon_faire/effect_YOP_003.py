"""Effect for Luckysoul Hoarder (YOP_003).

Card Text: [x]<b>Battlecry:</b> Shuffle 2 Soul
Fragments into your deck.
<b>Corrupt:</b> Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)