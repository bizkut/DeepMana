"""Effect for Grand Empress Shek'zara (DMF_516).

Card Text: <b>Battlecry:</b> <b>Discover</b> a card in your deck and draw all copies of it.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)