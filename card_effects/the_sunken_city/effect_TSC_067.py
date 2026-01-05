"""Effect for Ambassador Faelin (TSC_067).

Card Text: <b>Battlecry:</b> Put 3 <b>Colossal</b> minions on the bottom of your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass