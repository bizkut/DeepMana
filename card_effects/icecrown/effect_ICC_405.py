"""Effect for Rotface (ICC_405).

Card Text: [x]After this minion
survives damage,
summon a random
<b>Legendary</b> minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ICC_405t")