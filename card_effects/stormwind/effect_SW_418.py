"""Effect for SI:7 Skulker (SW_418).

Card Text: [x]<b>Stealth</b>
<b>Battlecry:</b> The next card
  you draw costs (1) less.
"""

from simulator.enums import CardType

def battlecry(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(1)