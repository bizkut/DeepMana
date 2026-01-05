"""Effect for Skydiving Instructor (YOD_028).

Card Text: [x]<b>Battlecry:</b> Summon a
1-Cost minion from
your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "YOD_028t")