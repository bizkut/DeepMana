"""Effect for Frantic Hippogryph (AV_215).

Card Text: <b>Rush</b>. <b>Honorable Kill</b>:
 Gain <b>Windfury</b>. 
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass