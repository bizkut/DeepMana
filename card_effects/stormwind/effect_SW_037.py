"""Effect for Irebound Brute (SW_037).

Card Text: [x]<b>Taunt</b>
Costs (1) less for each
card drawn this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)