"""Effect for Shepherd's Crook (EDR_416).

Card Text: After your hero attacks, summon a 3/3 Sheep that's <b>Dormant</b> for 2 turns.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_416t")