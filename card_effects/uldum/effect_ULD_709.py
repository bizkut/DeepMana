"""Effect for Armored Goon (ULD_709).

Card Text: Whenever your hero attacks, gain 5 Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(5)