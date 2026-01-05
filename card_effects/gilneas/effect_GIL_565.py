"""Effect for Deathweb Spider (GIL_565).

Card Text: <b>Battlecry:</b> If your hero
took damage this turn, gain <b>Lifesteal</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass