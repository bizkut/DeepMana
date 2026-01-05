"""Effect for Golakka Crawler (UNG_807).

Card Text: <b>Battlecry:</b> Destroy a Pirate and gain +1/+1.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()