"""Effect for Teacher's Pet (SCH_244).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Summon a
random 3-Cost Beast.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_244t")