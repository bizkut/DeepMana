"""Effect for Wizened Truthseeker (TIME_057).

Card Text: <b>Battlecry:</b> Set the Cost of every card in both player's hands back to their original Costs.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass