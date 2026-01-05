"""Effect for Embers of Strength (RLK_960).

Card Text: [x]Summon two 1/2
Guards with <b>Taunt</b>.
<b>Manathirst (6):</b> Give
them +1/+2.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "RLK_960t")