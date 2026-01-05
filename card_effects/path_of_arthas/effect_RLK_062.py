"""Effect for Nerubian Swarmguard (RLK_062).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Summon two
copies of this minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_062t")