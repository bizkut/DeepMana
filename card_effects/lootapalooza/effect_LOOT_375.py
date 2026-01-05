"""Effect for Guild Recruiter (LOOT_375).

Card Text: <b>Battlecry:</b> <b>Recruit</b> a minion that costs (4) or less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass