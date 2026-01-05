"""Effect for Double Jump (SCH_422).

Card Text: Draw an <b>Outcast</b> card from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)