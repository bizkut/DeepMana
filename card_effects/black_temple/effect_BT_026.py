"""Effect for Aldor Truthseeker (BT_026).

Card Text: <b>Taunt</b>. <b>Battlecry:</b> Reduce the Cost of your Librams by (2) this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass