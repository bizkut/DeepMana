"""Effect for Reaper's Scythe (SCH_238).

Card Text: [x]<b>Spellburst</b>: Also
damages adjacent
minions this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass