"""Effect for High Inquisitor Whitemane (EX1_190).

Card Text: <b>Battlecry:</b> Summon all friendly minions that died this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EX1_190t")