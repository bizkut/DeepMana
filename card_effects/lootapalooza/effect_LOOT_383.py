"""Effect for Hungry Ettin (LOOT_383).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Summon a random 2-Cost minion for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_383t")