"""Effect for Cannonmaster Smythe (BAR_879).

Card Text: <b>Battlecry:</b> Transform your <b>Secrets</b> into 3/3 Soldiers. They transform back when they die.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass