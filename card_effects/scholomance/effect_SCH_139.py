"""Effect for Devout Pupil (SCH_139).

Card Text: [x]<b>Divine Shield, Taunt</b>
Costs (1) less for each spell
you've cast on friendly
characters this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass