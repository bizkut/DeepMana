"""Effect for Harbinger of the Blighted (EDR_781).

Card Text: [x]Whenever this enters your
hand from the battlefield,
summon two random
2-Cost minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_781t")