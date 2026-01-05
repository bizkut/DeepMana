"""Effect for Cheat Death (LOOT_204).

Card Text: <b>Secret:</b> When a friendly minion dies, return it to your hand.
It costs (2) less.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass