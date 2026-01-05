"""Effect for Justicar Trueheart (CORE_AT_132).

Card Text: <b>Battlecry:</b> Replace your starting Hero Power with a better one.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass