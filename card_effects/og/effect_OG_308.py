"""Effect for Giant Sand Worm (OG_308).

Card Text: Whenever this attacks and kills a minion, it may attack again.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass