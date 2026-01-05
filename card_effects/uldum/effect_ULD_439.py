"""Effect for Sandwasp Queen (ULD_439).

Card Text: <b>Battlecry:</b> Add two 2/1 Sandwasps to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass