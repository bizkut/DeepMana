"""Effect for Glowroot Lure (EDR_477).

Card Text: [x]<b>Taunt</b>. Costs (1) less for
each time you used your
Hero Power this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass