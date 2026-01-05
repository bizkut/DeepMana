"""Effect for Totem Goliath (SCH_615).

Card Text: <b>Deathrattle:</b> Summon all four basic Totems.
<b>Overload:</b> (1)
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_615t")