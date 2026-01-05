"""Effect for Anima Golem (GVG_077).

Card Text: At the end of each turn, destroy this minion if it's your only one.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()