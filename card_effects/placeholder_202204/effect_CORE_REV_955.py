"""Effect for Stewart the Steward (CORE_REV_955).

Card Text: [x]<b>Deathrattle:</b> Give the next
Silver Hand Recruit you
summon +3/+3 and
this <b>Deathrattle</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_955t")