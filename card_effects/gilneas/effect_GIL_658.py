"""Effect for Splintergraft (GIL_658).

Card Text: [x]<b>Battlecry:</b> Choose a friendly
minion. Add a 10/10 copy to
your hand that costs (10).
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass