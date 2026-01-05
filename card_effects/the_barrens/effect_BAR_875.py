"""Effect for Sword of the Fallen (BAR_875).

Card Text: [x]After your hero attacks,
cast a <b>Secret</b> from
your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass