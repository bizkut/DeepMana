"""Effect for Ancharrr (DRG_025).

Card Text: After your hero attacks, draw a Pirate from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)