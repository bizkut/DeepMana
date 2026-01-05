"""Effect for Asphyxiate (RLK_087).

Card Text: Destroy the highest Attack enemy minion.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()