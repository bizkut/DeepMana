"""Effect for Jade Spirit (CFM_715).

Card Text: <b>Battlecry:</b> Summon a{1} {0} <b>Jade Golem</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "CFM_715t")