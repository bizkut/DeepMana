"""Effect for Cult Apothecary (OG_295).

Card Text: <b>Battlecry:</b> For each enemy minion, restore #2 Health to your hero.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)