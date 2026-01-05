"""Effect for Commanding Shout (NEW1_036).

Card Text: Your minions can't be reduced below 1 Health this turn. Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)