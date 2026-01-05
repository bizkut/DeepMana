"""Effect for Snowfall Graveyard (AV_400).

Card Text: [x]Your <b>Deathrattles</b>
trigger twice.
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass