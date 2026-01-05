"""Effect for Kel'Thuzad, the Inevitable (REV_514).

Card Text: [x]<b>Battlecry:</b> Resurrect your 
Volatile Skeletons. Any that 
can't fit on the battlefield 
instantly explode! 0
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass