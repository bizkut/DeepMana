"""Effect for Smolderthorn Lancer (TRL_326).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, destroy a damaged enemy minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()