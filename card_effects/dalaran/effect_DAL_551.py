"""Effect for Proud Defender (DAL_551).

Card Text: <b>Taunt</b>
Has +2 Attack while you [x]have no other minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2