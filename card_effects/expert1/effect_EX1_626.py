"""Effect for Mass Dispel (EX1_626).

Card Text: <b>Silence</b> all enemy minions. Draw a card.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)