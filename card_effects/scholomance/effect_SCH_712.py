"""Effect for Judicious Junior (SCH_712).

Card Text: <b>Lifesteal</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass