"""Effect for Past Conflux (TIME_436).

Card Text: [x]Summon a random Dragon
that costs (5) or more.
<i>Advance to the present!</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TIME_436t")