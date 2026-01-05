"""Effect for Ram Wrangler (AT_010).

Card Text: <b>Battlecry:</b> If you have a Beast, summon a
random Beast.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "AT_010t")