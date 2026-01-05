"""Effect for Selfish Shellfish (TSC_935).

Card Text: <b>Deathrattle:</b> Your opponent draws 2 cards.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    player.draw(2)