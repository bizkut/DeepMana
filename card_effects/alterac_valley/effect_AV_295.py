"""Effect for Capture Coldtooth Mine (AV_295).

Card Text: <b>Choose One -</b> Draw your lowest Cost card;
or Draw your highest
Cost card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)