"""Effect for Spirit of the Dragonhawk (TRL_319).

Card Text: [x]<b>Stealth</b> for 1 turn.
Your Hero Power also targets
 adjacent minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass