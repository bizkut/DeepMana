"""Effect for Psychic Scream (LOOT_008).

Card Text: Shuffle all minions into your opponent's deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass