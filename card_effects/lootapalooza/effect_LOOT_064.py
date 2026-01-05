"""Effect for Lesser Sapphire Spellstone (LOOT_064).

Card Text: Summon 1 copy of a friendly minion. <i>(<b>Overload</b> 3 Mana Crystals to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_064t")