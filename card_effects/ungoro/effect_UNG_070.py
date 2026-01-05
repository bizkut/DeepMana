"""Effect for Tol'vir Stoneshaper (UNG_070).

Card Text: [x]<b>Battlecry:</b> If you played an
Elemental last turn, gain
 <b>Taunt</b> and <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass