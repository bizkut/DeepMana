"""Effect for Onyx Bishop (KAR_204).

Card Text: <b>Battlecry:</b> Summon a random friendly minion
that died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "KAR_204t")