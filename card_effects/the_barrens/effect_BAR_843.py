"""Effect for Warsong Envoy (BAR_843).

Card Text: [x]<b>Frenzy:</b> Gain +1 Attack
for each damaged
 character.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1