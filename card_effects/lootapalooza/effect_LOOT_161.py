"""Effect for Carnivorous Cube (LOOT_161).

Card Text: <b>Battlecry:</b> Destroy
a friendly minion.
<b>Deathrattle:</b> Summon 2 copies of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_161t")


def deathrattle(game, source):
    pass