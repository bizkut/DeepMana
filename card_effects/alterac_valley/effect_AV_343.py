"""Effect for Stonehearth Vindicator (AV_343).

Card Text: [x]<b>Battlecry:</b> Draw a spell
that costs (3) or less.
It costs (0) this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)