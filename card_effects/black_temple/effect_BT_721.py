"""Effect for Blistering Rot (BT_721).

Card Text: [x]At the end of your turn,
summon a Rot with stats
equal to this minion's.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "BT_721t")