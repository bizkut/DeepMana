"""Effect for Rising Winds (YOD_001).

Card Text: <b>Twinspell</b>
<b>Choose One -</b> Draw a card; or Summon a 3/2 Eagle.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)