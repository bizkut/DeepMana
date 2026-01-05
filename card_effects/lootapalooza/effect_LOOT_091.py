"""Effect for Lesser Pearl Spellstone (LOOT_091).

Card Text: Summon a 2/2 Spirit with <b>Taunt</b>. <i>(Restore 3 Health to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_091t")