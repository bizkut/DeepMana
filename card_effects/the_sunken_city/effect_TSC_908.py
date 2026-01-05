"""Effect for Sir Finley, Sea Guide (TSC_908).

Card Text: [x]<b>Battlecry:</b> Swap your
hand with the bottom of
your deck.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass