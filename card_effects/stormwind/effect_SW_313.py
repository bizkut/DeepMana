"""Effect for Rise to the Occasion (SW_313).

Card Text: <b>Questline:</b> Play 3 different 1-Cost cards.
<b>Reward:</b> Equip a 1/4 Light's Justice.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass