"""Effect for Imp-oster (CORE_MAW_000).

Card Text: <b>Battlecry:</b> Choose a friendly Imp. Transform into a copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass