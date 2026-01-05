"""Effect for Kor'kron Elite (NEW1_011).

Card Text: <b>Charge</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass