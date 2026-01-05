"""Effect for Encumbered Pack Mule (SW_306).

Card Text: [x]<b>Taunt</b>
When you draw this, add a
 copy of it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)