"""Effect for Frostwolf Grunt (CS2_121).

Card Text: <b>Taunt</b>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass