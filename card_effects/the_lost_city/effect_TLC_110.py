"""Effect for City Chief Esho (TLC_110).

Card Text: [x]<b>Battlecry:</b> If every minion in
your deck shares a minion type,
give your other minions +2/+2
<i>(wherever they are)</i>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2