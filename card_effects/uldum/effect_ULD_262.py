"""Effect for High Priest Amet (ULD_262).

Card Text: [x]Whenever you summon a
minion, set its Health equal
to this minion's.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "ULD_262t")