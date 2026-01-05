"""Effect for Mimiron's Head (GVG_111).

Card Text: At the start of your turn, if you have at least 3 Mechs, destroy them all and form V-07-TR-0N.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()