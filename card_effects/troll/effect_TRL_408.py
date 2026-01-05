"""Effect for Grave Horror (TRL_408).

Card Text: [x]<b>Taunt</b>
Costs (1) less for each spell
you've cast this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass