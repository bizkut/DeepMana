"""Effect for Partner in Crime (REV_247).

Card Text: [x]<b>Battlecry:</b> Summon a 
copy of this minion at 
the end of your turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_247t")