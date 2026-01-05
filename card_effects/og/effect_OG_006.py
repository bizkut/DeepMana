"""Effect for Vilefin Inquisitor (OG_006).

Card Text: <b>Battlecry:</b> Your Hero Power becomes 'Summon a   1/1 Murloc.'
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "OG_006t")