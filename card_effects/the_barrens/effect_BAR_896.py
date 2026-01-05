"""Effect for Stonemaul Anchorman (BAR_896).

Card Text: [x]<b>Rush</b>
<b>Frenzy:</b> Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)