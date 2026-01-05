"""Effect for Mount Hyjal Imposter (WON_077).

Card Text: [x]Each turn this is in your
hand, transform it into a
random 4-Cost minion
that gains <b>Stealth</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass