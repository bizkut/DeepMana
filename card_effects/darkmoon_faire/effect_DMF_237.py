"""Effect for Carnival Barker (DMF_237).

Card Text: Whenever you summon a 1-Health minion, give it +1/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_237t")