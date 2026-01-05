"""Effect for Stealer of Souls (WC_023).

Card Text: The first card you draw each turn costs Health instead of Mana.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)