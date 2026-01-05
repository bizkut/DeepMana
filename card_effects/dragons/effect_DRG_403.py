"""Effect for Blowtorch Saboteur (DRG_403).

Card Text: <b>Battlecry:</b> Your opponent's next Hero Power costs (2) more.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass