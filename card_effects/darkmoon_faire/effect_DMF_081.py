"""Effect for K'thir Ritualist (DMF_081).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Add a random
4-Cost minion to your
opponent's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass