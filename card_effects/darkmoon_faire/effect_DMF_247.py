"""Effect for Insatiable Felhound (DMF_247).

Card Text: <b>Taunt</b>
 <b>Corrupt:</b> Gain +1/+1 and <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1