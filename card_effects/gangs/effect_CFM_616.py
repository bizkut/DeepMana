"""Effect for Pilfered Power (CFM_616).

Card Text: Gain an empty Mana Crystal for each friendly minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass