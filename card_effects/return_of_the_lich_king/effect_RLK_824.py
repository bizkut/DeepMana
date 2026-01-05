"""Effect for Arms Dealer (RLK_824).

Card Text: After you summon an Undead, give it +1 Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_824t")