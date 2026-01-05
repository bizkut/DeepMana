"""Effect for Aquatic Form (TSC_654).

Card Text: <b>Dredge</b>. If you have the Mana to play the card this turn, draw it.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)