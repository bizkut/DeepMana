"""Effect for Waterboy (TRL_407).

Card Text: <b>Battlecry:</b> Your next Hero Power this turn costs (0).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass