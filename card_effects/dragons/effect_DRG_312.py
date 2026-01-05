"""Effect for Shrubadier (DRG_312).

Card Text: <b>Battlecry:</b> Summon a 2/2 Treant.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_312t")