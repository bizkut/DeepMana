"""Effect for Pit Master (DMF_703).

Card Text: <b>Battlecry:</b> Summon a 3/2 Duelist.
<b>Corrupt:</b> Summon two.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_703t")