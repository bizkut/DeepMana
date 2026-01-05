"""Effect for Dalaran Librarian (DAL_735).

Card Text: <b>Battlecry:</b> <b>Silence</b>
adjacent minions.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.silence(target)