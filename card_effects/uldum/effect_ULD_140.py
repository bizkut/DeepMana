"""Effect for Supreme Archaeology (ULD_140).

Card Text: <b>Quest:</b> Draw 20 cards.
<b>Reward:</b> Tome of Origination.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(20)