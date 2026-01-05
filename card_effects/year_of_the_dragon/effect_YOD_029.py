"""Effect for Hailbringer (YOD_029).

Card Text: [x]<b>Battlecry:</b> Summon two 1/1
Ice Shards that <b>Freeze</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_029t")