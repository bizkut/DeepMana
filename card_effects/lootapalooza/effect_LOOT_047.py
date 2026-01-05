"""Effect for Barkskin (LOOT_047).

Card Text: Give a minion +3 Health. Gain 3 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 3, source)