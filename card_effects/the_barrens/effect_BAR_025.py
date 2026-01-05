"""Effect for Sunwell Initiate (BAR_025).

Card Text: <b>Frenzy:</b> Gain <b>Divine Shield</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass