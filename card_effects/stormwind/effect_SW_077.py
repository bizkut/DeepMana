"""Effect for Stockades Prisoner (SW_077).

Card Text: [x]Starts <b>Dormant</b>.
After you play 3 cards,
this awakens.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass