"""Effect for Galakrond, the Tempest (DRG_620).

Card Text: [x]<b>Battlecry:</b> Summon two
2/2 Storms with <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_620t")