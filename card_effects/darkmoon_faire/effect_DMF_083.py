"""Effect for Dancing Cobra (DMF_083).

Card Text: <b>Corrupt:</b> Gain <b>Poisonous</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass