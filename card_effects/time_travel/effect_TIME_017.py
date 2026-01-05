"""Effect for Tankgineer (TIME_017).

Card Text: [x]<b>Divine Shield</b>
<b>Deathrattle:</b> Summon a 7/7
Tank with <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_017t")