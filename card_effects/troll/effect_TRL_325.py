"""Effect for Sul'thraze (TRL_325).

Card Text: <b>Overkill</b>: You may attack again.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass