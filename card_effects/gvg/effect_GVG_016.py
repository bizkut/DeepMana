"""Effect for Fel Reaver (GVG_016).

Card Text: Whenever your opponent plays a card, remove the top 3 cards of your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass