"""Effect for Sewer Crawler (LOOT_069).

Card Text: <b>Battlecry:</b> Summon a 2/3 Giant Rat.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_069t")