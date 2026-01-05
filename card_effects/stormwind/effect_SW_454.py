"""Effect for Lion's Frenzy (SW_454).

Card Text: Has Attack equal to the number of cards you've drawn this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)