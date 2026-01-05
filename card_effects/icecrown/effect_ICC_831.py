"""Effect for Bloodreaver Gul'dan (ICC_831).

Card Text: <b>Battlecry:</b> Summon all friendly Demons that died this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_831t")