"""Effect for Mosh'Ogg Announcer (TRL_532).

Card Text: [x]Enemies attacking this
have a 50% chance to
attack someone else.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass