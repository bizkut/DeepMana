"""Effect for Boneweb Egg (SCH_147).

Card Text: [x]<b>Deathrattle:</b> Summon
two 2/1 Spiders. If you
discard this, trigger its
<b>Deathrattle</b>.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_147t")