"""Effect for Stubborn Suspect (SW_006).

Card Text: <b>Deathrattle:</b> Summon a random 3-Cost minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SW_006t")