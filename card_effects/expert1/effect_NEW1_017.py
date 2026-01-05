"""Effect for Hungry Crab (NEW1_017).

Card Text: <b>Battlecry:</b> Destroy a Murloc and gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()