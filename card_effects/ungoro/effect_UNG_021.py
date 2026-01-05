"""Effect for Steam Surger (UNG_021).

Card Text: [x]<b>Battlecry:</b> If you played
an Elemental last turn,
add a 'Flame Geyser'
to your hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass