"""Effect for Mischief Maker (ULD_229).

Card Text: <b>Battlecry:</b> Swap the top card of your deck with your opponent's.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass