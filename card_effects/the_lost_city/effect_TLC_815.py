"""Effect for Gravedawn Voidbulb (TLC_815).

Card Text: Summon a random 4-Cost minion and
give it <b>Taunt</b>.
<b>Kindred:</b> Do it again.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TLC_815t")