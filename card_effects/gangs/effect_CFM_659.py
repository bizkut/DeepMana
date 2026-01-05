"""Effect for Gadgetzan Socialite (CFM_659).

Card Text: <b>Battlecry:</b> Restore #2 Health.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 2, source)