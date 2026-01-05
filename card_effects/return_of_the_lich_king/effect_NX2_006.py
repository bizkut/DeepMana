"""Effect for Jolly Roger (NX2_006).

Card Text: After your hero
attacks, summon a
1/1 Undead Pirate.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "NX2_006t")