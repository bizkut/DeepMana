"""Effect for Nethrandamus (BT_481).

Card Text: [x]<b>Battlecry:</b> Summon two
random 0-Cost minions.
<i>(Upgrades each time a
friendly minion dies!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_481t")