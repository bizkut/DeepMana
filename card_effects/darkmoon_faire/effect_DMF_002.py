"""Effect for N'Zoth, God of the Deep (DMF_002).

Card Text: <b>Battlecry:</b> Resurrect a friendly minion of each minion type.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass