"""Effect for Remote-Controlled Golem (SW_097).

Card Text: [x]After this takes damage,
shuffle two Golem Parts into
your deck. When drawn,
  summon a 2/1 Mech.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(2)