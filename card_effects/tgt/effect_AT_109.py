"""Effect for Argent Watchman (AT_109).

Card Text: Can't attack.
<b>Inspire:</b> Can attack as normal this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass