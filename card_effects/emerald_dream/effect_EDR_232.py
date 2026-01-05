"""Effect for Typhoon (EDR_232).

Card Text: Each minion gets shuffled into a random player's deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass