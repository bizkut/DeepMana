"""Effect for Secret Passage (SCH_305).

Card Text: Replace your hand with 4 cards from your deck. Swap back next turn.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass