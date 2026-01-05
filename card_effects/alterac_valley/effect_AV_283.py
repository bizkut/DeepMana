"""Effect for Rune of the Archmage (AV_283).

Card Text: [x]Cast 20 Mana worth of
Mage spells at enemies.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass