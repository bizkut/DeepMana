"""Effect for Juicy Psychmelon (BOT_404).

Card Text: Draw a 7, 8, 9, and
10-Cost minion
 from your deck.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(7)