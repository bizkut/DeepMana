"""Effect for Sword of Justice (EX1_366).

Card Text: After you summon a minion, give it +1/+1 and this loses 1 Durability.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EX1_366t")