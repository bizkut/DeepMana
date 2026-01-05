"""Effect for Zaqali Flamemancer (FIR_940).

Card Text: <b>Battlecry:</b> If every card in your hand is of a different Cost, reduce their Costs by (2).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass