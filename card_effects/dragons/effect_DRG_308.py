"""Effect for Mindflayer Kaahrj (DRG_308).

Card Text: <b>Battlecry:</b> Choose an
enemy minion.
<b>Deathrattle:</b> Summon a new copy of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DRG_308t")


def deathrattle(game, source):
    pass