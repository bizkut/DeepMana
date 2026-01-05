"""Effect for Elder Longneck (UNG_109).

Card Text: <b>Battlecry:</b> If you're holding a minion with 5 or more Attack, <b>Adapt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass