"""Effect for Druid of the Fang (GVG_080).

Card Text: <b>Battlecry:</b> If you have a Beast, transform this minion into a 7/7.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass