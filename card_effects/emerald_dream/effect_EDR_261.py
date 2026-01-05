"""Effect for Amphibian's Spirit (EDR_261).

Card Text: [x]Give a minion +2/+2
and "<b>Deathrattle:</b> Give a
friendly minion +2/+2
and this <b>Deathrattle</b>."
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2