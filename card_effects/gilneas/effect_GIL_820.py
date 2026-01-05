"""Effect for Shudderwock (GIL_820).

Card Text: [x]<b>Battlecry:</b> Repeat all other
<b>Battlecries</b> from cards you
played this game <i>(targets
chosen randomly)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass