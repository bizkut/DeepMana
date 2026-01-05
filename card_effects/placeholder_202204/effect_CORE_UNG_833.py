"""Effect for Lakkari Felhound (CORE_UNG_833).

Card Text: <b>Taunt</b>
<b>Battlecry:</b> Discard your two lowest-Cost cards.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass