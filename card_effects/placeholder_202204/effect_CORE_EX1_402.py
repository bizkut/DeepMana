"""Effect for Armorsmith (CORE_EX1_402).

Card Text: Whenever a friendly minion takes damage, gain 1 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(1)