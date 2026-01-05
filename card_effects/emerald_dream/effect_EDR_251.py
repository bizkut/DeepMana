"""Effect for Dragonscale Armaments (EDR_251).

Card Text: Draw a spell that started in your deck and one that didn't.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)