"""Effect for Feign Death (GVG_026).

Card Text: Trigger all <b>Deathrattles</b> on your minions.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass