"""Effect for Lesser Diamond Spellstone (CORE_LOOT_507).

Card Text: Resurrect 2 different friendly minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass