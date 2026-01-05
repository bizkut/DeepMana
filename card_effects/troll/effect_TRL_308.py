"""Effect for High Priest Thekal (TRL_308).

Card Text: <b>Battlecry:</b> Convert all but 1 of your Hero's Health into Armor.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)