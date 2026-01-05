"""Effect for Halkias (REV_829).

Card Text: [x]<b>Stealth</b>. <b>Deathrattle:</b> Store
Halkias's soul inside of a
friendly <b>Secret</b>. It resummons
Halkias when triggered.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_829t")