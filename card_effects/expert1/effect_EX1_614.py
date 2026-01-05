"""Effect for Xavius (EX1_614).

Card Text: After you play a card, summon a 2/1 Satyr.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EX1_614t")