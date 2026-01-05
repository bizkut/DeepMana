"""Effect for Rabble Bouncer (TRL_515).

Card Text: <b>Taunt</b>
Costs (1) less for each enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass