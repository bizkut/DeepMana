"""Effect for Sightless Magistrate (MAW_008).

Card Text: <b>Battlecry:</b> Both players draw
until they have 5 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)