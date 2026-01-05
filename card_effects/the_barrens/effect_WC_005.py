"""Effect for Primal Dungeoneer (WC_005).

Card Text: [x]<b>Battlecry:</b> Draw a spell.
If it's a Nature spell, also
draw an Elemental.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)