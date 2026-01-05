"""Effect for Sheldras Moontree (SW_447).

Card Text: [x]<b>Battlecry:</b> The next 3
spells you draw are
<b>Cast When Drawn</b>.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(3)