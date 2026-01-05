"""Effect for Hulking Overfiend (BT_487).

Card Text: <b>Rush</b>. After this attacks and kills a minion, it may attack again.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass