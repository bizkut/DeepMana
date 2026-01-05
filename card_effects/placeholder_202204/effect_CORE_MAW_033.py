"""Effect for Sylvanas, the Accused (CORE_MAW_033).

Card Text: [x]<b>Battlecry:</b> Destroy
an enemy minion.
<b>Infuse (7):</b> Take control
of it instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()