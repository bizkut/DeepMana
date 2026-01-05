"""Effect for Abominable Bowman (CORE_ICC_825).

Card Text: [x]<b>Deathrattle:</b> Summon
a random friendly Beast
that died this game.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_ICC_825t")