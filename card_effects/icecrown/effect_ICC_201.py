"""Effect for Roll the Bones (ICC_201).

Card Text: Draw a card.
If it has <b>Deathrattle</b>, cast this again.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)