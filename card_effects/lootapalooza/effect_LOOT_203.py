"""Effect for Lesser Mithril Spellstone (LOOT_203).

Card Text: Summon one 5/5 Mithril Golem. <i>(Equip a weapon to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "LOOT_203t")