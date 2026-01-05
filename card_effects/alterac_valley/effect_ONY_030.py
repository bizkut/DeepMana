"""Effect for SI:7 Smuggler (ONY_030).

Card Text: [x]<b>Battlecry:</b> Summon a random
1-Cost minion. <i>(Upgraded
for each other SI:7 card you
 have played this game.)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ONY_030t")