"""Effect for Class Action Lawyer (CORE_MAW_017).

Card Text: [x]<b>Battlecry:</b> If your deck
has no Neutral cards, set
 a minion's stats to 1/1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass