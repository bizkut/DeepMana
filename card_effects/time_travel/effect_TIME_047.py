"""Effect for Devious Coyote (TIME_047).

Card Text: [x]<b>Stealth</b>. Costs (1) less for
each time the enemy hero
took damage this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass