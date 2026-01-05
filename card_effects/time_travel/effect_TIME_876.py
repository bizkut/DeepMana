"""Effect for Shapeshifter (TIME_876).

Card Text: [x]Each turn this is in your
hand, transform into a
random minion in your
opponent's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass