"""Effect for Sleep Paralysis (EDR_490).

Card Text: [x]<b>Choose One - </b>Summon
two 3/6 Demons with
<b>Taunt</b> that can't attack; or
Destroy an enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "EDR_490t")