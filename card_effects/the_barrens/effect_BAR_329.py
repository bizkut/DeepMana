"""Effect for Death Speaker Blackthorn (BAR_329).

Card Text: <b>Battlecry:</b> Summon 3 <b>Deathrattle</b> minions that cost (5) or less from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BAR_329t")


def deathrattle(game, source):
    pass