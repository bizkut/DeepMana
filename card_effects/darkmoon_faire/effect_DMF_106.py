"""Effect for Occult Conjurer (DMF_106).

Card Text: <b>Battlecry:</b> If you control a <b>Secret</b>, summon a copy of this.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_106t")