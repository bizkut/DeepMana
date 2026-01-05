"""Effect for Zola the Gorgon (CORE_LOOT_516).

Card Text: <b>Battlecry:</b> Choose a friendly minion. Add a Golden copy of it to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass