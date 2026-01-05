"""Effect for Cult Master (EX1_595).

Card Text: After a friendly minion dies, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)