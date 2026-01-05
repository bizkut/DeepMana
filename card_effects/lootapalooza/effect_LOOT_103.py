"""Effect for Lesser Ruby Spellstone (LOOT_103).

Card Text: Add 1 random Mage spell to your hand. <i>(Play 2 Elementals to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass