"""Effect for Hooked Reaver (LOOT_018).

Card Text: <b>Battlecry:</b> If you have 15 or less Health, gain +3/+3 and <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 15, source)