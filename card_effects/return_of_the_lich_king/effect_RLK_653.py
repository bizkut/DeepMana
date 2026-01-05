"""Effect for Infectious Ghoul (RLK_653).

Card Text: [x]<b>Deathrattle:</b> Give a
random friendly minion
"<b>Deathrattle:</b> Summon an
Infectious Ghoul."
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_653t")