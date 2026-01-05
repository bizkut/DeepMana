"""Effect for Famished Fool (REV_019).

Card Text: <b>Battlecry:</b> Draw a card.
<b>Infuse (4):</b> Draw 3 instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)