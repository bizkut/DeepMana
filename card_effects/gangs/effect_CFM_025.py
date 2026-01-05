"""Effect for Wind-up Burglebot (CFM_025).

Card Text: Whenever this attacks a minion and survives, draw a card.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)