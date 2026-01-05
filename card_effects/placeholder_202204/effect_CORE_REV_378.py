"""Effect for Forensic Duster (CORE_REV_378).

Card Text: [x]<b>Battlecry:</b> Your 
opponent's minions 
cost (1) more next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass