"""Effect for Servant of Yogg-Saron (OG_087).

Card Text: [x]<b>Battlecry:</b> Cast a random
 spell that costs (5) or MORE 
 <i>(targets chosen randomly)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass