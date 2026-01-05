"""Effect for Libram of Wisdom (BT_025).

Card Text: [x]Give a minion +1/+1
and "<b>Deathrattle:</b> Add
a 'Libram of Wisdom'
spell to your hand."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1