"""Effect for Investment Opportunity (SW_095).

Card Text: [x]Draw an <b>Overload</b> card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)