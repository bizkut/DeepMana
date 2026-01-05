"""Effect for Twisted Tether (RLK_537).

Card Text: Destroy a minion.
Give its stats to a random Undead in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    import random
    if opponent.board: random.choice(list(opponent.board)).destroy()