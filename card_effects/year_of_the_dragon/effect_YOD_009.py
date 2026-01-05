"""Effect for The Amazing Reno (YOD_009).

Card Text: <b>Battlecry:</b> Make all minions disappear. <i>*Poof!*</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass