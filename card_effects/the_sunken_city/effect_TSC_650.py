"""Effect for Flipper Friends (TSC_650).

Card Text: [x]<b>Choose One</b> - Summon a
6/6 Orca with <b>Taunt</b>; or
six 1/1 Otters with <b>Rush</b>.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TSC_650t")