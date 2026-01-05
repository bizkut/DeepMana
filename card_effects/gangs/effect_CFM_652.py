"""Effect for Second-Rate Bruiser (CFM_652).

Card Text: [x]<b>Taunt</b>
Costs (2) less if your
opponent has at least
three minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass