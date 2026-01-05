"""Effect for Enter the Coliseum (AT_078).

Card Text: Destroy all minions except each player's highest Attack minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()