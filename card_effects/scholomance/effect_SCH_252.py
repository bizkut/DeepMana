"""Effect for Marrowslicer (SCH_252).

Card Text: <b>Battlecry:</b> Shuffle 2 Soul Fragments into your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass