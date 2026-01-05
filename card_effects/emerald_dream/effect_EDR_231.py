"""Effect for Aspect's Embrace (EDR_231).

Card Text: [x]Restore #4 Health.
Draw a card.
<b>Imbue</b> your Hero Power.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)