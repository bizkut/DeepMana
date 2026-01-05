"""Effect for Blademaster Okani (TSC_032).

Card Text: [x]<b>Battlecry:</b> <b>Secretly</b> choose to
<b>Counter</b> the next minion or
spell your opponent plays
while this is alive.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass