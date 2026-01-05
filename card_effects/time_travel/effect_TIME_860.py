"""Effect for Faceless Enigma (TIME_860).

Card Text: [x]<b>Battlecry:</b> Look at 2 random
<b>Secrets</b>. Pick one to cast for
yourself. The other casts
for your opponent.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass