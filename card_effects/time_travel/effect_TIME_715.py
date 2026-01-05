"""Effect for For Glory! (TIME_715).

Card Text: Draw 2 cards. Costs
(1) less for each minion your opponent controls.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)