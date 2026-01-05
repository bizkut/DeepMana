"""Effect for Chronochiller (TIME_617).

Card Text: You no longer draw a card at the start of your turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)