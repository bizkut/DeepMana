"""Effect for Sanguine Reveler (CORE_ICC_903).

Card Text: <b>Battlecry:</b> Destroy a friendly minion and gain +2/+2.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()