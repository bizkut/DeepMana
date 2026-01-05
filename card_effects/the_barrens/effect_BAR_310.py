"""Effect for Lightshower Elemental (BAR_310).

Card Text: [x]<b>Taunt</b>
<b>Deathrattle:</b> Restore #8 Health
to all friendly characters.
"""

from simulator.enums import CardType

def deathrattle(game, source):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 8, source)