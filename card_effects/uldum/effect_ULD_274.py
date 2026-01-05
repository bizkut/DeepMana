"""Effect for Wasteland Assassin (ULD_274).

Card Text: <b>Stealth</b>
<b>Reborn</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass