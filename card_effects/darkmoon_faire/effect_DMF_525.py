"""Effect for Ringmaster Whatley (DMF_525).

Card Text: <b>Battlecry:</b> Draw a Mech, Dragon, and Pirate.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)