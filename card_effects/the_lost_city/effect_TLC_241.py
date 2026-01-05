"""Effect for Ido of the Threshfleet (TLC_241).

Card Text: [x]While this is alive,
you get a 2-Cost Holy spell
that gives a minion +2/+2
and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2