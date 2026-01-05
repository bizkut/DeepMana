"""Effect for Lucentbark (DAL_357).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Go <b>Dormant</b>. Restore 5 Health to awaken this minion.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)