"""Effect for Incorporeal Corporal (RLK_117).

Card Text: After this minion attacks,
destroy it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()