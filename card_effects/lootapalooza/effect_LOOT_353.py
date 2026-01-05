"""Effect for Psionic Probe (LOOT_353).

Card Text: Copy a spell in your opponent's deck and add it to your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass