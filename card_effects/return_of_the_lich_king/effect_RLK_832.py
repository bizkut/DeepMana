"""Effect for High Cultist Basaleph (RLK_832).

Card Text: <b>Battlecry:</b> Resurrect all friendly Undead that died after your last turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass