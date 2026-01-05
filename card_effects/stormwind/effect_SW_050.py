"""Effect for Maestra of the Masquerade (SW_050).

Card Text: You start the game as a different class until you play a Rogue card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass