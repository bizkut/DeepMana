"""Effect for Restore the Wild (TLC_239).

Card Text: <b>Quest:</b> Fill your board
on 3 of your turns.
<b>Reward:</b> The Everbloom.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass