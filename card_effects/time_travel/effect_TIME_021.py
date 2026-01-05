"""Effect for Doomsday Prepper (TIME_021).

Card Text: <b>Outcast:</b> Your hero is <b>Immune</b> until your
next turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass