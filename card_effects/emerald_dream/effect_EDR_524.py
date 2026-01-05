"""Effect for Shadowcloaked Assailant (EDR_524).

Card Text: [x]<b>Battlecry:</b> If you're holding
one of the same cards as
your opponent, shuffle
theirs into their deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass