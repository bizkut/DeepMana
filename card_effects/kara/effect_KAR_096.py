"""Effect for Prince Malchezaar (KAR_096).

Card Text: [x]<b>Start of Game:</b>
Add 5 extra <b>Legendary</b>
minions to your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass