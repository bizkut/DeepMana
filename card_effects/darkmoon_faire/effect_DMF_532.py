"""Effect for Circus Amalgam (DMF_532).

Card Text: <b>Taunt</b>
<i>This has all minion types.</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass