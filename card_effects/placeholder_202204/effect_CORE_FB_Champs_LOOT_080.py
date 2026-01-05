"""Effect for Lesser Emerald Spellstone (CORE_FB_Champs_LOOT_080).

Card Text: Summon two 3/3 Wolves. <i>(Play a <b>Secret</b> to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_FB_Champs_LOOT_080t")