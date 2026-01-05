"""Effect for Ozruk (UNG_907).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Gain +5 Health
for each Elemental you
played last turn.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 5, source)