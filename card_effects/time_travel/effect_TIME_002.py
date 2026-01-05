"""Effect for Aeon Wizard (TIME_002).

Card Text: [x]<b>Rewind</b>
<b>Battlecry:</b> Get 2 random
spells from your class.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass