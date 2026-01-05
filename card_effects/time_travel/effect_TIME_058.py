"""Effect for Paltry Flutterwing (TIME_058).

Card Text: [x]<b>Deathrattle:</b> Summon a
random 2-Cost minion that
is <b>Dormant</b> for 2 turns.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_058t")