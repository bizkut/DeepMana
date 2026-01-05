"""Effect for Lesser Diamond Spellstone (LOOT_507).

Card Text: Resurrect 2 different friendly minions. <i>(Cast 4 spells to upgrade.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass