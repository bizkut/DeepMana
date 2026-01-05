"""Effect for Aluneth (LOOT_108).

Card Text: At the end of your turn, draw 3 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)