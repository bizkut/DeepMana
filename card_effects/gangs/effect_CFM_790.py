"""Effect for Dirty Rat (CFM_790).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Your opponent
summons a random minion
from their hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_790t")