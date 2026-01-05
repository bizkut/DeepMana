"""Effect for Furnacefire Colossus (CORE_ICC_096).

Card Text: <b>Battlecry:</b> Discard all weapons from your hand and gain their stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass