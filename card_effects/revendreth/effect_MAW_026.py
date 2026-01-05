"""Effect for Incarceration (MAW_026).

Card Text: [x]Choose a minion.
It goes <b>Dormant</b>
for 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass