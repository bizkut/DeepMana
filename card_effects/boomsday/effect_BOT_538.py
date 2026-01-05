"""Effect for Spark Engine (BOT_538).

Card Text: <b>Battlecry:</b> Add a 
1/1 Spark with <b>Rush</b> to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass