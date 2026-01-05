"""Effect for Battle Rage (EX1_392).

Card Text: Draw a card for each damaged friendly character.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)