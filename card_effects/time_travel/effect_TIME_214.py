"""Effect for Flux Revenant (TIME_214).

Card Text: [x]<b>Taunt</b>
Whenever you would damage
this with a Nature spell, it
gains +2/+1 instead.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2