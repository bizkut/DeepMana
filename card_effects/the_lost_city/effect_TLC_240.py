"""Effect for Tyrannogill (TLC_240).

Card Text: [x]<b>Rush</b>
<b>Deathrattle:</b> Summon three
2/1 Murlocs. Give them each
a random <b>Bonus Effect</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_240t")