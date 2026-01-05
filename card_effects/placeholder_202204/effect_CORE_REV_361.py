"""Effect for Wild Spirits (CORE_REV_361).

Card Text: [x]Summon two different 
<b>Dormant</b> Wildseeds. 
Make your Wildseeds 
awaken 1 turn sooner.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_361t")