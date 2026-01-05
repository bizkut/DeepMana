"""Effect for Bazaar Mugger (ULD_327).

Card Text: <b>Rush</b>
<b>Battlecry:</b> Add a random minion from another class to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass