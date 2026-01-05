"""Effect for Nobleman (SW_074).

Card Text: <b>Battlecry:</b> Create a Golden copy of a random card in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass