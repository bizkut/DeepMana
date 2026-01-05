"""Effect for Warden of Chains (AV_262).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If you're holding
a Demon that costs (5) or
more, gain +1/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5