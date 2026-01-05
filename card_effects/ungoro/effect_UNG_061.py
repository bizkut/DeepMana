"""Effect for Obsidian Shard (UNG_061).

Card Text: Costs (1) less for each non-Rogue Class card added to your hand this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass