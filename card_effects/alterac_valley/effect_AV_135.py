"""Effect for Stormpike Marshal (AV_135).

Card Text: [x]<b>Taunt</b>
If you took 5 or more damage
on your opponent's turn,
this costs (1).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass