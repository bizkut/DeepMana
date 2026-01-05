"""Effect for Steamcleaner (REV_946).

Card Text: <b>Battlecry:</b> Destroy ALL cards in both players' decks that didn't start there.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: target.destroy()