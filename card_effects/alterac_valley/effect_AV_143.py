"""Effect for Korrak the Bloodrager (AV_143).

Card Text: [x]<b>Deathrattle:</b> If this
wasn't <b>Honorably Killed</b>,
resummon Korrak.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_143t")