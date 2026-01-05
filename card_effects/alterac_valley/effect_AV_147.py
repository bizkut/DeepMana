"""Effect for Dun Baldar Bunker (AV_147).

Card Text: [x]At the end of your
turn, draw a <b>Secret</b> and
set its Cost to (1).
Lasts 3 turns.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)