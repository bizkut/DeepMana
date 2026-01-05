"""Effect for Cornelius Roame (SW_080).

Card Text: [x]At the start and end
 of each player's turn,
draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)