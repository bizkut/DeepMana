"""Effect for Krag'wa, the Frog (TRL_345).

Card Text: <b>Battlecry:</b> Return all spells you played last turn to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass