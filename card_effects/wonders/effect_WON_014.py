"""Effect for Invigorate (WON_014).

Card Text: <b>Choose One -</b> Gain an empty Mana Crystal; or Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)