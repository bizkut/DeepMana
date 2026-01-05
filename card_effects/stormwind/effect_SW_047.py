"""Effect for Highlord Fordragon (SW_047).

Card Text: [x]<b>Divine Shield</b>
After a friendly minion loses
<b>Divine Shield</b>, give a minion
  in your hand +5/+5.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 5
        target._max_health += 5