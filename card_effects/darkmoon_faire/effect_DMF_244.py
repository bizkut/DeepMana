"""Effect for Day at the Faire (DMF_244).

Card Text: Summon 3 Silver
Hand Recruits.
<b>Corrupt:</b> Summon 5.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "DMF_244t")