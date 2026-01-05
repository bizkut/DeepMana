"""Effect for Deranged Doctor (GIL_118).

Card Text: <b>Deathrattle:</b> Restore #8 Health to your hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)