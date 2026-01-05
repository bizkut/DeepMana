"""Effect for Free Admission (DMF_113).

Card Text: Draw 2 minions. If they're both Demons, reduce their Costs by (2).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)