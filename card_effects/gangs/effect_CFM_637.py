"""Effect for Patches the Pirate (CFM_637).

Card Text: [x]After you play a Pirate,
summon this minion
from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_637t")