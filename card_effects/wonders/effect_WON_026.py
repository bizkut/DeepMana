"""Effect for Durnholde Imposter (WON_026).

Card Text: [x]Each turn this is in your
hand, transform it into a
random 3-Cost minion
that gains <b>Poisonous</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass