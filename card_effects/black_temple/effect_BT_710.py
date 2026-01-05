"""Effect for Greyheart Sage (BT_710).

Card Text: [x]<b>Battlecry:</b> If you control
a <b><b>Stealth</b>ed</b> minion,
draw 2 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)