"""Effect for Void Terror (VAN_EX1_304).

Card Text: [x]<b>Battlecry:</b> Destroy both
adjacent minions and gain
 their Attack and Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()