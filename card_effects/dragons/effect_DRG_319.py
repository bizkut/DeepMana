"""Effect for Goru the Mightree (DRG_319).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> For the rest of
the game, your Treants
have +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1