"""Effect for Volcoross (FIR_951).

Card Text: [x]<b>Rush, Taunt</b>
<b>Battlecry:</b> Choose to spend
10, 20, or 30 <b>Corpses</b> to
gain that many stats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass