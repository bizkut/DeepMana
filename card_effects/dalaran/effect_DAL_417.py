"""Effect for Heistbaron Togwaggle (DAL_417).

Card Text: <b>Battlecry:</b> If you control a <b>Lackey</b>, choose a fantastic treasure.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass