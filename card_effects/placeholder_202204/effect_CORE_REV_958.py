"""Effect for Buffet Biggun (CORE_REV_958).

Card Text: [x]<b>Battlecry:</b> Summon two Silver 
Hand Recruits. <b>Infuse (3):</b> 
Give them +2 Attack 
and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_958t")