"""Effect for Sister Svalna (RLK_816).

Card Text: <b>Battlecry:</b> <i>Permanently</i> add a Vision of Darkness to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass