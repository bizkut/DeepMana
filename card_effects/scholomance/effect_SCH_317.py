"""Effect for Playmaker (SCH_317).

Card Text: [x]After you play a <b>Rush</b>
minion, summon a copy
 with 1 Health remaining.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "SCH_317t")