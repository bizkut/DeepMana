"""Effect for Bladed Lady (DMF_226).

Card Text: [x]<b>Rush</b>
Costs (1) if your hero has
6 or more Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass