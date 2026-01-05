"""Effect for Fatebreaker (TIME_028).

Card Text: [x]<b>Lifesteal</b>
<b>Battlecry:</b> Cast a Shred
of Time from your deck
to gain +3/+3.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3