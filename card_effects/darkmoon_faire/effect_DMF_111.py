"""Effect for Man'ari Mosher (DMF_111).

Card Text: <b>Battlecry:</b> Give a friendly Demon +3 Attack and <b>Lifesteal</b> this turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 3
        target._max_health += 3