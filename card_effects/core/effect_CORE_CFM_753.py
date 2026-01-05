"""Effect for Grimestreet Outfitter (CORE_CFM_753).

Card Text: <b>Battlecry:</b> Give all minions in your hand +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent
    pass
