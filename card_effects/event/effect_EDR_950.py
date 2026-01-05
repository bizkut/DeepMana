"""Effect for Sharp-Eyed Lookout (EDR_950).

Card Text: <b>Battlecry:</b> Draw a card.
It costs (1) less this turn.
<i>(I know its name!)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)