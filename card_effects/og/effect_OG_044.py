"""Effect for Fandral Staghelm (OG_044).

Card Text: Your <b>Choose One</b> cards and powers have both effects combined.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass