"""Effect for Might of Menethil (CORE_RLK_740).

Card Text: <b>Battlecry:</b> Spend
up to 3 <b>Corpses</b>.
<b>Freeze</b> that many
enemy minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.frozen = True