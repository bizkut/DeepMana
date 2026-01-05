"""Effect for Ghastly Conjurer (ICC_069).

Card Text: <b>Battlecry:</b> Add a 'Mirror Image' spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass