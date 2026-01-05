"""Effect for Shieldbreaker (TRL_524).

Card Text: <b>Battlecry:</b> <b>Silence</b> an enemy minion with <b>Taunt</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)