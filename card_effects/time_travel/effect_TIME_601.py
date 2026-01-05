"""Effect for Arrow Retriever (TIME_601).

Card Text: <b>Battlecry:</b> Draw until you have 3 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)