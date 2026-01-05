"""Effect for Shard of the Naaru (CORE_SW_441).

Card Text: <b>Tradeable</b>
<b>Silence</b> all enemy minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)