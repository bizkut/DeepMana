"""Effect for Crimson Clergy (CS3_014).

Card Text: <b>Overheal:</b> Draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)