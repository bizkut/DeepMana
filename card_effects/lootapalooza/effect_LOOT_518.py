"""Effect for Windshear Stormcaller (LOOT_518).

Card Text: <b>Battlecry:</b> If you control all 4 basic Totems, summon Al'Akir the Windlord.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_518t")