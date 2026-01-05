"""Effect for Charged Call (SW_035).

Card Text: [x]<b>Discover</b> a 1-Cost
minion and summon it. 
<i>(Upgraded for each <b>Overload</b>
 card you played this game!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_035t")