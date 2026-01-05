"""Effect for Coral Keeper (TSC_648).

Card Text: [x]<b>Battlecry:</b> Summon a
3/3 Elemental for each
spell school you've
cast this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_648t")