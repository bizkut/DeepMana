"""Effect for Carrion Drake (GIL_905).

Card Text: <b>Battlecry:</b> If a minion died this turn, gain <b>Poisonous</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass