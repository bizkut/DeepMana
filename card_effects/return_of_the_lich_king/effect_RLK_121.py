"""Effect for Acolyte of Death (RLK_121).

Card Text: After a friendly Undead dies, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)