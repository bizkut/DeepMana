"""Effect for Siphoning Growth (EDR_531).

Card Text: Destroy a friendly
minion to gain 8 Armor.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()