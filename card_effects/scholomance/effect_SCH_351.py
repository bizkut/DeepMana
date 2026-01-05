"""Effect for Jandice Barov (SCH_351).

Card Text: [x]<b>Battlecry:</b> Summon two
random 5-Cost minions.
Secretly pick one that dies
 when it takes damage.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_351t")