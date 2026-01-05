"""Effect for Wildpaw Gnoll (AV_298).

Card Text: [x]<b>Rush</b>
Costs (1) less for each
non-Rogue Class card added
to your hand this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass