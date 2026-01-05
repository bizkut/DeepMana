"""Effect for Mirage Caller (UNG_022).

Card Text: <b>Battlecry:</b> Choose a minion. Summon a 1/1 copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "UNG_022t")