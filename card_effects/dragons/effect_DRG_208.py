"""Effect for Valdris Felgorge (DRG_208).

Card Text: <b>Battlecry:</b> Increase your maximum hand size to 12. Draw 4 cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(12)