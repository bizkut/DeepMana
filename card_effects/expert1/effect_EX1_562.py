"""Effect for Onyxia (EX1_562).

Card Text: <b>Battlecry:</b> Summon 1/1 Whelps until your side of the battlefield is full.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EX1_562t")