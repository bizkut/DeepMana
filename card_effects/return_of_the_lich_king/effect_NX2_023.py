"""Effect for The Purator (NX2_023).

Card Text: [x]<b>Taunt</b>
<b>Battlecry:</b> If your deck has no
Neutral cards, draw a minion
of each minion type.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)