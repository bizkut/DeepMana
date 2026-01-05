"""Effect for Smoldering Grove (FIR_911).

Card Text: Draw {0} card.
<i>(Upgrades each turn,
but discards after {1}!)</i>1Draw {0} cards.
<i>(Discards this turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    player.draw(0)