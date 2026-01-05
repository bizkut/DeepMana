"""Effect for Doppelgangster (CFM_668).

Card Text: <b>Battlecry:</b> Summon 2 copies of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_668t")