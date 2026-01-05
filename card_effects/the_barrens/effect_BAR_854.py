"""Effect for Kindling Elemental (BAR_854).

Card Text: [x]<b>Battlecry:</b> The next
 Elemental you play
costs (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass