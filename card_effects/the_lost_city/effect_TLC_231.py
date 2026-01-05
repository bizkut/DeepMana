"""Effect for Story of Barnabus (TLC_231).

Card Text: Draw a minion.
If it has 5 or more Attack, give it +5 Health and gain 5 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)