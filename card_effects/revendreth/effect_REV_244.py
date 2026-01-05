"""Effect for Mischievous Imp (REV_244).

Card Text: <b>Battlecry:</b> Summon a copy of this. <b>Infuse (3):</b> Summon two copies instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_244t")