"""Effect for Kobold Hermit (LOOT_062).

Card Text: <b>Battlecry:</b> Choose a basic Totem. Summon it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_062t")