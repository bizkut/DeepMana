"""Effect for Nithogg (DRG_224).

Card Text: [x]<b>Battlecry:</b> Summon two
0/3 Eggs. Next turn they
hatch into 4/4 Drakes
with <b>Rush</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_224t")