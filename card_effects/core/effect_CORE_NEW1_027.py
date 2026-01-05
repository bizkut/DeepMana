"""Effect for Southsea Captain (CORE_NEW1_027).

Card Text: Your other Pirates have +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
