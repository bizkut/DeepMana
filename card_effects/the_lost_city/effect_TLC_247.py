"""Effect for Primal Sabretooth (TLC_247).

Card Text: [x]<b>Stealth</b>
After this attacks and kills a
minion, get a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass