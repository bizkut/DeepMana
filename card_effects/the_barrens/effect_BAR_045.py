"""Effect for Arid Stormer (BAR_045).

Card Text: <b>Battlecry:</b> If you played an Elemental last turn, gain <b>Rush</b> and <b>Windfury</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass