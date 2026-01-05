"""Effect for Command of Neptulon (TID_005).

Card Text: Summon two 5/4 Elementals with <b>Rush</b>.
<b>Overload:</b> (1)
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TID_005t")