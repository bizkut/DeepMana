"""Effect for Oaken Summons (CORE_LOOT_309).

Card Text: Gain 6 Armor.
Summon a minion
from your deck that
costs (4) or less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_LOOT_309t")