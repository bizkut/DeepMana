"""Effect for Keening Banshee (CORE_ICC_911).

Card Text: Whenever you play a card, remove the top 3 cards of your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass