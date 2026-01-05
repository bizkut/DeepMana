"""Effect for Unidentified Maul (LOOT_286).

Card Text: Gains a bonus effect in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass