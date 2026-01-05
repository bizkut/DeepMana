"""Effect for Djinni of Zephyrs (LOE_053).

Card Text: After you cast a spell on another friendly minion, cast a copy of it on this one.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass