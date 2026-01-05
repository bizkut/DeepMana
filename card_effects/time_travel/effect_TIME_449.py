"""Effect for Lasting Legacy (TIME_449).

Card Text: [x]Give your hero
+4 Attack this turn. If your
deck has no minions, give
any in hand +4 Attack.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 4
        target._max_health += 4