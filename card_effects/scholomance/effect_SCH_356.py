"""Effect for Glide (SCH_356).

Card Text: [x]Shuffle your hand into
your deck. Draw 4 cards.
<b>Outcast:</b> Your opponent
does the same.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(4)