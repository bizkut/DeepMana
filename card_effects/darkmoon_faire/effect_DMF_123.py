"""Effect for Open the Cages (DMF_123).

Card Text: [x]<b>Secret:</b> When your
turn starts, if you control
 two minions, summon an
Animal Companion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_123t")