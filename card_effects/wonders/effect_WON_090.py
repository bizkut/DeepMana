"""Effect for Pebbly Page (WON_090).

Card Text: [x]<b>Battlecry:</b> Draw an
<b>Overload</b> card. You can't
be <b>Overloaded</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)