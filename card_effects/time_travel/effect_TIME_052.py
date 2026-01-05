"""Effect for Amber Warden (TIME_052).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Summon a
random minion from
the past.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_052t")