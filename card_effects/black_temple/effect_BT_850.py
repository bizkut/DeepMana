"""Effect for Magtheridon (BT_850).

Card Text: [x]<b>Dormant</b>. <b>Battlecry:</b> Summon
three 1/3 enemy Warders.
When they die, destroy all
minions and awaken.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_850t")