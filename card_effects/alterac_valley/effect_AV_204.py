"""Effect for Kurtrus, Demon-Render (AV_204).

Card Text: [x]<b>Battlecry:</b> Summon two
1/4 Demons with <b>Rush</b>.
<i>(Improved by your hero
attacks this game.)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AV_204t")