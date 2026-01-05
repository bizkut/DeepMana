"""Effect for Parachute Brigand (DRG_056).

Card Text: [x]After you play a Pirate,
summon this minion
from your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_056t")