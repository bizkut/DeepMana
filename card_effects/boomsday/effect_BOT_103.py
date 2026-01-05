"""Effect for Stargazer Luna (BOT_103).

Card Text: After you play the
right-most card in your hand, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)