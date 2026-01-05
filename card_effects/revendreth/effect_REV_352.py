"""Effect for Stonebound Gargon (REV_352).

Card Text: [x]<b>Rush</b>
<b>Infuse (3):</b> Also damages
the minions next to
  whomever this attacks.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass