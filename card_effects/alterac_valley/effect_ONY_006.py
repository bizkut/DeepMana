"""Effect for Deep Breath (ONY_006).

Card Text: [x]Deal $1 damage to a
minion and its neighbors.
<i>(Improved by number of 
other spells in your hand.)</i>
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target: game.deal_damage(target, 1, source)