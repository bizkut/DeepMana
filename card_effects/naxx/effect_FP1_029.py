"""Effect for Dancing Swords (FP1_029).

Card Text: <b>Deathrattle:</b> Your opponent draws a card.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(1)