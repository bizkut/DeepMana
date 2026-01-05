"""Effect for Millhouse Manastorm (VAN_NEW1_029).

Card Text: <b>Battlecry:</b> Enemy spells cost (0) next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass