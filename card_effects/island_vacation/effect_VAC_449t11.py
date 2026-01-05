"""Effect for Carress, Cabaret Star (VAC_449t11).

Card Text: [x]<b>Battlecry:</b> Gain +2/+2 and <b>Taunt</b>. <b>Freeze</b> three random enemy minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
