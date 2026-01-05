"""Effect for Priestess Valishj (TSC_828).

Card Text: [x]<b>Battlecry:</b> Refresh an empty
Mana Crystal for each spell
   you've cast this turn.@ <i>(@)</i>
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass