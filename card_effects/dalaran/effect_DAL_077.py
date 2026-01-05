"""Effect for Toxfin (DAL_077).

Card Text: <b>Battlecry:</b> Give a friendly Murloc <b>Poisonous</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 1
        target._max_health += 1