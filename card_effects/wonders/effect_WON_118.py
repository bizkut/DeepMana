"""Effect for Jade Spirit (WON_118).

Card Text: <b>Battlecry:</b> Summon a{1} {0} <b>Jade Golem</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "WON_118t")