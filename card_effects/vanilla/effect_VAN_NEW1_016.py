"""Effect for Captain's Parrot (VAN_NEW1_016).

Card Text: <b>Battlecry:</b> Draw a Pirate from your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)