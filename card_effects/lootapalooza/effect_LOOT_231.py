"""Effect for Arcane Artificer (LOOT_231).

Card Text: Whenever you cast a spell, gain Armor equal to its Cost.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(1)