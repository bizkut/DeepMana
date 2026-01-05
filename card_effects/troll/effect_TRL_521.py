"""Effect for Arena Patron (TRL_521).

Card Text: <b>Overkill:</b> Summon another Arena Patron.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    game.summon_token(player, "TRL_521t")