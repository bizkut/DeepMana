"""Effect for Dwarven Sharpshooter (DRG_253).

Card Text: Your Hero Power can target minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass