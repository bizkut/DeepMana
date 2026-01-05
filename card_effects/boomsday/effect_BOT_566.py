"""Effect for Reckless Experimenter (BOT_566).

Card Text: [x]<b>Deathrattle</b> minions you
play cost (3) less, but die
at the end of the turn.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    pass