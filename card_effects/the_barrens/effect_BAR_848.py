"""Effect for Lilypad Lurker (BAR_848).

Card Text: [x]<b>Battlecry:</b> If you played an
Elemental last turn, transform
an enemy minion into a
0/1 Frog with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass