"""Effect for Spellbreaker (EX1_048).

Card Text: <b>Battlecry:</b> <b>Silence</b> a minion.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)