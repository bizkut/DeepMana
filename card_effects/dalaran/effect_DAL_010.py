"""Effect for Togwaggle's Scheme (DAL_010).

Card Text: Choose a minion. Shuffle 1 copy of it into your deck.
<i>(Upgrades each turn!)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    pass