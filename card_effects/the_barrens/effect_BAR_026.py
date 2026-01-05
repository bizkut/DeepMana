"""Effect for Death's Head Cultist (BAR_026).

Card Text: <b>Taunt</b>
<b>Deathrattle:</b> Restore 4 Health to your hero.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 4, source)