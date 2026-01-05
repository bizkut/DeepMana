"""Effect for Game Master (DMF_102).

Card Text: The first <b>Secret</b> you play each turn costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass