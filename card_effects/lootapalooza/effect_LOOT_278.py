"""Effect for Unidentified Elixir (LOOT_278).

Card Text: Give a minion +2/+2. Gains a bonus effect in your hand.
"""

from simulator.enums import CardType

def on_play(game, source, target):
    player = source.controller
    opponent = player.opponent

    if target:
        target._attack += 2
        target._max_health += 2