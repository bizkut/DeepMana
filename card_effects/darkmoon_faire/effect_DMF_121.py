"""Effect for Fortune Teller (DMF_121).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Gain +1/+1 for
each spell in your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1