"""Effect for Enter the Lost City (TLC_602).

Card Text: [x]<b>Quest:</b> Survive 10 turns.
<b>Reward: </b>Latorvius, Gaze
of the City.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass