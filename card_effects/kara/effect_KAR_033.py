"""Effect for Book Wyrm (KAR_033).

Card Text: <b>Battlecry:</b> If you're holding a Dragon, destroy an enemy minion with 3 or less Attack.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()