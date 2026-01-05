"""Effect for Sethekk Veilweaver (BT_254).

Card Text: [x]After you cast a spell on
a minion, add a Priest
spell to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass