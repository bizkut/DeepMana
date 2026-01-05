"""Effect for Starving Buzzard (CS2_237).

Card Text: Whenever you summon a Beast, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)