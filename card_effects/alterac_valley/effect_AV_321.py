"""Effect for Glory Chaser (AV_321).

Card Text: After you play a <b>Taunt</b> minion, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)