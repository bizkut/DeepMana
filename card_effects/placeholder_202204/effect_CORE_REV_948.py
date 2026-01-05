"""Effect for Service Bell (CORE_REV_948).

Card Text: <b>Discover</b> a Class card from your deck and draw all copies of it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)