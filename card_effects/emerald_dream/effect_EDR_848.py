"""Effect for Photosynthesis (EDR_848).

Card Text: Restore #6 Health. Get 3 random Druid spells.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 6, source)