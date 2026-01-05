"""Effect for Deathwing the Destroyer (LEG_CS3_036).

Card Text: <b>Battlecry:</b> Destroy all other minions. Discard a card for each destroyed.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()