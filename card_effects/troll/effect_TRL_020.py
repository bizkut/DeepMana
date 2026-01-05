"""Effect for Sightless Ranger (TRL_020).

Card Text: <b>Rush</b>
<b>Overkill</b>: Summon two 1/1 Bats.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_020t")