"""Effect for Sinstone Graveyard (REV_750).

Card Text: [x]Summon a 1/1 Ghost.
<i>(Has +1/+1 for each other
card you played this turn!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "REV_750t")