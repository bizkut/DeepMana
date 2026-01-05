"""Effect for Shield Block (EX1_606).

Card Text: Gain 5 Armor.
Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(5)