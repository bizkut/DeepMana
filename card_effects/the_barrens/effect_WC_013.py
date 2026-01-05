"""Effect for Devout Dungeoneer (WC_013).

Card Text: [x]<b>Battlecry:</b> Draw a spell.
If it's a Holy spell,
reduce its Cost by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)