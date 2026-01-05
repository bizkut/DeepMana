"""Effect for Raid the Docks (SW_028).

Card Text: [x]<b>Questline:</b> Play 3 Pirates.
<b>Reward:</b> Draw a weapon.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)