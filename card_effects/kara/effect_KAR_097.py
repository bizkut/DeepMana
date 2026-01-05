"""Effect for Medivh, the Guardian (KAR_097).

Card Text: <b>Battlecry:</b> Equip Atiesh, Greatstaff of the Guardian.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass