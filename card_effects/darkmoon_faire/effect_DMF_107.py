"""Effect for Rigged Faire Game (DMF_107).

Card Text: <b>Secret:</b> If you didn't take any damage during your opponent's turn, draw 3 cards.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)