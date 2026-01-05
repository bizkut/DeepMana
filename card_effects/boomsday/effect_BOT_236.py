"""Effect for Crystalsmith Kangor (BOT_236).

Card Text: <b>Divine Shield</b>, <b>Lifesteal</b>
Your healing is doubled.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)