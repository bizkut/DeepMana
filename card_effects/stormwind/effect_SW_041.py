"""Effect for Sigil of Alacrity (SW_041).

Card Text: [x]At the start of your next
turn, draw a card and
 reduce its Cost by (1).
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)