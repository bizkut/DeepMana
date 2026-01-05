"""Effect for Masked Reveler (CORE_REV_015).

Card Text: [x]<b>Rush</b>
<b>Deathrattle:</b> Summon
a 2/2 copy of another
minion in your deck.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_015t")