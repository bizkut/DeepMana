"""Effect for Oasis Surger (ULD_292).

Card Text: <b>Rush</b>
<b>Choose One -</b> Gain +2/+2; or Summon a copy of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_292t")