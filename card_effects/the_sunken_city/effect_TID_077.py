"""Effect for Lightray (TID_077).

Card Text: <b>Taunt</b>
Costs (1) less for each Paladin card you've played this game.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass