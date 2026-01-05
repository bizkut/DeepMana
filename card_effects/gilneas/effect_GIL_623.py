"""Effect for Witchwood Grizzly (GIL_623).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> Lose 1 Health
for each card in your
opponent's hand.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.heal(target, 1, source)