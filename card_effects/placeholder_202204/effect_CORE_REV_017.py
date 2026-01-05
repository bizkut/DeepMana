"""Effect for Insatiable Devourer (CORE_REV_017).

Card Text: [x]<b>Battlecry:</b> Devour an enemy 
minion and gain its stats. 
 <b>Infuse (5):</b> And its neighbors.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass