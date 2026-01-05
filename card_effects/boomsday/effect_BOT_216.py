"""Effect for Omega Medic (BOT_216).

Card Text: <b>Battlecry:</b> If you have 10 Mana Crystals, restore #10 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 10, source)