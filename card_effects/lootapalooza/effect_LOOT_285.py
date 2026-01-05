"""Effect for Unidentified Shield (LOOT_285).

Card Text: Gain 5 Armor.
Gains a bonus effect in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if player.hero: player.hero.gain_armor(5)