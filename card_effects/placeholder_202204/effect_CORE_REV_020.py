"""Effect for Dinner Performer (CORE_REV_020).

Card Text: [x]<b>Battlecry:</b> Summon a
random minion from
your deck that you
can afford to play.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CORE_REV_020t")