"""Effect for Gonk, the Raptor (TRL_241).

Card Text: After your hero attacks and kills a minion, it may attack again.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass