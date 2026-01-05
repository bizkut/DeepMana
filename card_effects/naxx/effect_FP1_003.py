"""Effect for Echoing Ooze (FP1_003).

Card Text: <b>Battlecry:</b> Summon an exact copy of this minion at the end of the turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "FP1_003t")