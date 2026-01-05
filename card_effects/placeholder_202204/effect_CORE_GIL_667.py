"""Effect for Rotten Applebaum (CORE_GIL_667).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Restore #6 Health to your hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 6, source)